import os
import sys
from typing import Dict

import mlflow
from neuro_mf import ModelFactory

from src.constant import training_pipeline
from src.entity.artifact_entity import (
    ClassifactionMetricArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact,
)
from src.entity.config_entity import ModelTrainerConfig
from src.exception import CustomException
from src.logger import logging
from src.ml.metric import calculate_metric
from src.ml.mlflow import MLFLowOperation
from src.ml.model.estimator import CustomModel
from src.utils.main_utils import load_csr_matrix, load_object, save_object


class ModelTrainer:
    def __init__(self, timestamp):
        self.model_trainer_config: ModelTrainerConfig = ModelTrainerConfig(
            timestamp=timestamp
        )

        self.data_transformation_artifact: DataTransformationArtifact = (
            DataTransformationArtifact(timestamp=timestamp)
        )

        self.mlflow_op = MLFLowOperation()

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

            vectorizer_obj = load_object(
                file_path=self.data_transformation_artifact.vectorized_file_path
            )

            model_factory = ModelFactory(
                model_config_path=self.model_trainer_config.model_config_file_path
            )

            best_model_detail = model_factory.get_best_model(
                X=X_train_features,
                y=y_train_targets,
                base_accuracy=self.model_trainer_config.expected_score,
            )

            if best_model_detail.best_score < self.model_trainer_config.expected_score:
                logging.info("No best model foudn with score more than base score")

                raise Exception("No best model found with score more than base score")

            for model in model_factory.grid_searched_best_model_list:
                with mlflow.start_run(
                    run_name=training_pipeline.EXP_NAME
                    + "-"
                    + model.model_serial_number
                ):

                    model_score: ClassifactionMetricArtifact = calculate_metric(
                        model=model.best_model, x=X_val_features, y=y_val_targets
                    )

                    model_parameters: Dict = model.best_parameters

                    trained_model = CustomModel(
                        preprocessor=vectorizer_obj, model=model.best_model
                    )

                    trained_model_path: str = os.path.join(
                        self.model_trainer_config.trained_model_file_dir,
                        trained_model.model.__class__.__name__
                        + "-"
                        + training_pipeline.EXP_NAME
                        + ".pkl",
                    )

                    save_object(file_path=trained_model_path, obj=trained_model)

                    self.mlflow_op.log_all_for_model(
                        model=trained_model,
                        model_parameters=model_parameters,
                        model_score=model_score.accuracy_score,
                    )

            mlflow.end_run()

            if best_model_detail.best_score < self.model_trainer_config.expected_score:
                logging.info("No best model found with score more than base score")

                raise Exception("No best model found with score more than base score")

            model_trainer_artifact: ModelTrainerArtifact = ModelTrainerArtifact(
                trained_model_list=model_factory.grid_searched_best_model_list,
                trained_model_dir=self.model_trainer_config.trained_model_file_dir,
                best_model_dir=self.model_trainer_config.best_model_file_dir,
                best_model_name=best_model_detail.best_model.__class__.__name__
                + "-"
                + training_pipeline.EXP_NAME,
            )

            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            raise CustomException(e, sys)
