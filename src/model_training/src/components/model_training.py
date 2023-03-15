import sys

from neuro_mf import ModelFactory
import json

from src.entity.artifact_entity import (
    ClassifactionMetricArtifact,
    DataTransformationArtifact,
    ModelInfoArtifact,
)
from src.entity.config_entity import ModelTrainerConfig
from src.exception import CustomException
from src.logger import logging
from src.ml.metric import calculate_metric
from src.utils.main_utils import load_csr_matrix, load_object, save_object


class ModelTrainer:
    def __init__(self, timestamp):
        self.model_trainer_config: ModelTrainerConfig = ModelTrainerConfig(
            timestamp=timestamp
        )

        self.data_transformation_artifact: DataTransformationArtifact = (
            DataTransformationArtifact(timestamp=timestamp)
        )

    def initiate_model_training(self):
        logging.info("Entered initiate_model_training method of ModelTrainer class")

        try:
            X_train_features = load_csr_matrix(
                file_path=self.data_transformation_artifact.transformed_train_features
            )

            y_train_targets = load_object(
                file_path=self.data_transformation_artifact.transformed_train_targets
            )

            X_val_features = load_csr_matrix(
                file_path=self.data_transformation_artifact.transformed_val_features
            )

            y_val_targets = load_object(
                file_path=self.data_transformation_artifact.transformed_val_targets
            )

            model_factory = ModelFactory(
                model_config_path=self.model_trainer_config.model_trainer_config_file_path
            )

            best_model_detail = model_factory.get_best_model(
                X=X_train_features,
                y=y_train_targets,
                base_accuracy=self.model_trainer_config.expected_accuracy,
            )

            if (
                best_model_detail.best_score
                < self.model_trainer_config.expected_accuracy
            ):
                logging.info("No best model foudn with score more than base score")

                raise Exception("No best model found with score more than base score")

            save_object(
                obj=best_model_detail.best_model,
                file_path=self.model_trainer_config.model_trainer_model_file_path,
            )

            model_metric: ClassifactionMetricArtifact = calculate_metric(
                best_model_detail.best_model, x=X_val_features, y=y_val_targets
            )

            best_model_info: ModelInfoArtifact = ModelInfoArtifact(
                model_name=best_model_detail.best_model.__class__.__name__,
                model_score=model_metric.__dict__,
                model_parameters=best_model_detail.best_parameters,
            )

            with open(
                self.model_trainer_config.model_trainer_best_model_info_path, "w"
            ) as f:
                json.dump(best_model_info.__dict__, f)

            logging.info(f"Best model info is : {best_model_info}")

            logging.info("Exited initiate_model_training method of ModelTrainer class")

        except Exception as e:
            raise CustomException(e, sys)
