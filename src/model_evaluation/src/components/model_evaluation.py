import json
import os
import sys

from src.cloud_storage.aws_storage import S3Operation
from src.entity.artifact_entity import (
    DataTransformationArtifact,
    ModelEvaluationArtifact,
    ModelTrainerArtifact,
)
from src.entity.config_entity import EvaluationModelResponse, ModelEvaluationConfig
from src.exception import CustomException
from src.logger import logging
from src.ml.metric import calculate_metric, get_model_score
from src.ml.model.estimator import get_s3_model
from src.utils.main_utils import load_object


class ModelEvaluation:
    def __init__(self, timestamp):
        self.model_trainer_artifact: ModelTrainerArtifact = ModelTrainerArtifact(
            timestamp=timestamp
        )

        self.model_evaluation_config: ModelEvaluationConfig = ModelEvaluationConfig(
            timestamp=timestamp
        )

        self.data_transformation_artifact: DataTransformationArtifact = (
            DataTransformationArtifact(timestamp=timestamp)
        )

        self.s3 = S3Operation()

    def evaluate_model(self):
        logging.info("Entered evaluate_model method of ModelEvaluation class")

        try:
            test_features = load_object(
                self.data_transformation_artifact.transformed_test_features
            )

            test_targets = load_object(
                self.data_transformation_artifact.transformed_test_targets
            )

            logging.info("Got the testing data")

            s3_model_path: str = get_s3_model(
                model_path=self.model_evaluation_config.model_evaluation_s3_model_path,
                bucket_name=self.model_evaluation_config.model_evaluation_s3_model_bucket,
            )

            logging.info(
                f"Got s3 model from {self.model_evaluation_config.model_evaluation_s3_model_bucket}"
            )

            trained_model_score: float = get_model_score(
                file_path=self.model_trainer_artifact.model_training_best_model_info
            )

            logging.info(f"Got the trained model score is {trained_model_score}")

            best_model_score = None

            if s3_model_path is not None:
                s3_model = load_object(
                    file_path=self.model_evaluation_config.model_evaluation_s3_model_path
                )

                s3_model_metric = calculate_metric(
                    model=s3_model, x=test_features, y=test_targets
                )

                best_model_score = s3_model_metric.accuracy_score

                logging.info(f"Best model score is {best_model_score}")

            tmp_best_model_score = 0 if best_model_score is None else best_model_score

            best_model_path = (
                None
                if not os.path.isfile(
                    self.model_evaluation_config.model_evaluation_s3_model_path
                )
                else self.model_evaluation_config.model_evaluation_s3_model_path
            )

            model_eval_result: EvaluationModelResponse = EvaluationModelResponse(
                trained_model_score=trained_model_score,
                best_model_score=best_model_score,
                is_model_accepted=trained_model_score > tmp_best_model_score,
                changed_score=trained_model_score - tmp_best_model_score,
                trained_model_path=self.model_trainer_artifact.model_training_best_model_path,
                best_model_path=best_model_path,
            )

            logging.info(f"Model Evaluation result : {model_eval_result}")

            logging.info("Exited evaluate_model method of ModelEvaluation class")

            return model_eval_result

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_model_evaluation(self):
        logging.info(
            "Entered initiate_model_evaluation method of ModelEvaluation class"
        )

        try:
            evaluation_model_response = self.evaluate_model()

            model_evaluation_result: ModelEvaluationArtifact = ModelEvaluationArtifact(
                is_model_accepted=evaluation_model_response.is_model_accepted,
                best_model_path=evaluation_model_response.best_model_path,
                trained_model_path=evaluation_model_response.trained_model_path,
            )

            os.makedirs(
                self.model_evaluation_config.model_evaluation_dir, exist_ok=True
            )

            with open(self.model_evaluation_config.model_evaluation_info, "w") as f:
                json.dump(model_evaluation_result.__dict__, f)

            logging.info(f"Model Evaluation Artifact is {model_evaluation_result}")

            logging.info(
                "Exited initiate_model_evaluation method of ModelEvaluation class"
            )

        except Exception as e:
            raise CustomException(e, sys)
