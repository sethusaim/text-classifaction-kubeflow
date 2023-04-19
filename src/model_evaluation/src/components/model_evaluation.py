import json
import os
import sys
from typing import Dict

import mlflow
from mlflow.models import EvaluationResult, MetricThreshold
from mlflow.models.evaluation.validation import ModelValidationFailedException

from src.entity.artifact_entity import (
    DataTransformationArtifact,
    ModelEvaluationArtifact,
    ModelTrainerArtifact,
)
from src.entity.config_entity import (
    EvaluationModelResponse,
    MLFlowModelInfo,
    ModelEvaluationConfig,
)
from src.exception import CustomException
from src.logger import logging
from src.ml.mlflow import MLFLowOperation
from src.utils.main_utils import load_object


class ModelEvaluation:
    def __init__(self, timestamp: str):
        self.model_trainer_artifact: ModelTrainerArtifact = ModelTrainerArtifact(
            timestamp=timestamp
        )

        self.model_evaluation_config: ModelEvaluationConfig = ModelEvaluationConfig(
            timestamp=timestamp
        )

        self.data_transformation_artifact: DataTransformationArtifact = (
            DataTransformationArtifact(timestamp=timestamp)
        )

        self.mlflow_op: MLFLowOperation = MLFLowOperation()

    def evaluate_model(self) -> EvaluationModelResponse:
        """
        This function evaluates a trained machine learning model by comparing it to a production model and
        returns an evaluation result.

        Returns:
          The method is returning an instance of the `EvaluationModelResponse` class.
        """
        logging.info("Entered evaluate_model method of ModelEvaluation class")

        try:
            model_eval_result = None

            test_features = load_object(
                file_path=self.data_transformation_artifact.transformed_test_features
            )

            test_targets = load_object(
                file_path=self.data_transformation_artifact.transformed_test_targets
            )

            logging.info("Got test features and targets")

            trained_model_info: MLFlowModelInfo = self.mlflow_op.get_model_info(
                best_model_path=self.model_trainer_artifact.model_training_best_model_dir
            )

            logging.info(f"Trained model info is {trained_model_info}")

            prod_model_info: MLFlowModelInfo = self.mlflow_op.get_prod_model_info()

            logging.info(f"Prod model info is {prod_model_info}")

            if prod_model_info is None:
                model_eval_result: EvaluationModelResponse = EvaluationModelResponse(
                    is_model_accepted=True,
                    trained_model_info=trained_model_info.__dict__,
                    accepted_model_info=trained_model_info.__dict__,
                    prod_model_info=None,
                )

                logging.info(f"Model evaluation result : {model_eval_result}")

                return model_eval_result

            else:
                eval_data = test_features

                eval_data["label"] = test_targets

                thresholds: Dict[str, MetricThreshold] = {
                    "score": MetricThreshold(
                        threshold=self.model_evaluation_config.model_eval_threshold,
                        min_absolute_change=self.model_evaluation_config.min_absolute_change,
                        higher_is_better=self.model_evaluation_config.higher_is_better,
                    )
                }

                try:
                    result: EvaluationResult = mlflow.evaluate(
                        model=trained_model_info.model_uri,
                        data=eval_data,
                        targets="label",
                        model_type=self.model_evaluation_config.model_type,
                        validation_thresholds=thresholds,
                        baseline_model=prod_model_info.model_uri,
                    )

                    model_eval_result: EvaluationModelResponse = (
                        EvaluationModelResponse(
                            is_model_accepted=True,
                            trained_model_info=trained_model_info.__dict__,
                            accepted_model_info=trained_model_info.__dict__,
                            prod_model_info=prod_model_info.__dict__,
                        )
                    )

                    logging.info(
                        f"MLFLow Model Evaluation Result is : {result.metrics}"
                    )

                    return model_eval_result

                except ModelValidationFailedException as e:
                    logging.info(
                        "Trained model is not better than the production model"
                    )

                    model_eval_result: EvaluationModelResponse = (
                        EvaluationModelResponse(
                            is_model_accepted=False,
                            trained_model_info=trained_model_info.__dict__,
                            accepted_model_info=None,
                            prod_model_info=prod_model_info.__dict__,
                        )
                    )

                    return model_eval_result

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_model_evaluation(self) -> ModelEvaluationArtifact:
        """
        This function initiates the evaluation of a machine learning model and saves the evaluation results
        as a JSON file.

        Returns:
          The method `initiate_model_evaluation` is returning an instance of the `ModelEvaluationArtifact`
        class.
        """
        logging.info(
            "Entered initiate_model_evaluation method of ModelEvaluation class"
        )

        try:
            evaluate_model_response: EvaluationModelResponse = self.evaluate_model()

            logging.info(f"Evaluation model response : {evaluate_model_response}")

            model_evaluation_artifact: ModelEvaluationArtifact = (
                ModelEvaluationArtifact(
                    is_model_accepted=evaluate_model_response.is_model_accepted,
                    trained_model_info=evaluate_model_response.trained_model_info,
                    accepted_model_info=evaluate_model_response.accepted_model_info,
                    prod_model_info=evaluate_model_response.prod_model_info,
                )
            )

            os.makedirs(
                self.model_evaluation_config.model_evaluation_dir, exist_ok=True
            )

            with open(self.model_evaluation_config.model_evaluation_info, "w") as f:
                json.dump(model_evaluation_artifact.__dict__, f)

            logging.info(f"Model Evaluation Artifact : {model_evaluation_artifact}")

            logging.info(
                "Exited initiate_model_evaluation method of ModelEvaluation class"
            )

            return model_evaluation_artifact

        except Exception as e:
            raise CustomException(e, sys)
