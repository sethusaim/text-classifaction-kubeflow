import sys

from src.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from src.entity.config_entity import ModelEvaluationConfig
from src.exception import EcomException
from src.logger import logging
from src.ml.metric import calculate_metric
from src.utils.main_utils import load_csr_matrix, load_object


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

    def evaluate_model(self):
        logging.info("Entered evaluate_model method of ModelEvaluation class")

        try:
            test_features = load_csr_matrix(
                self.data_transformation_artifact.transformed_test_features
            )

            test_targets = load_object(
                self.data_transformation_artifact.transformed_test_targets
            )

            logging.info("Got the testing data")

            logging.info("Exited evaluate_model method of ModelEvaluation class")

        except Exception as e:
            raise EcomException(e, sys)

    def initiate_model_evaluation(self):
        logging.info(
            "Entered initiate_model_evaluation method of ModelEvaluation class"
        )

        try:
            logging.info(
                "Exited initiate_model_evaluation method of ModelEvaluation class"
            )

        except Exception as e:
            raise EcomException(e, sys)
