import sys
from typing import Dict

from src.configuration.mlflow_connection import MLFlowClient
from src.entity.artifact_entity import ModelEvaluationArtifact
from src.entity.config_entity import ModelPusherConfig
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import read_json


class ModelPusher:
    def __init__(self, timestamp: str):
        self.model_evaluation_artifact = ModelEvaluationArtifact(timestamp=timestamp)

        self.model_pusher_config = ModelPusherConfig()

        self.mlflow_client = MLFlowClient().client

    def initiate_model_pusher(self):
        """
        This function initiates the process of pushing a trained model to production or staging based on its
        evaluation results.
        """
        logging.info("Entered initiate_model_pusher method of ModelPusher class")

        try:
            dic: Dict = read_json(
                file_path=self.model_evaluation_artifact.model_evaluation_info
            )

            if dic["accepted_model_info"] is None:
                raise Exception("No trained model is accepted")

            elif (
                dic["accepted_model_info"] is not None
                and dic["prod_model_info"] is None
            ):
                logging.info(
                    "Production model info is None, Accepted model info is not None. Moving accepted model to production"
                )

                self.mlflow_client.transition_model_version_stage(
                    name=dic["accepted_model_info"]["model_name"],
                    version=dic["accepted_model_info"]["model_version"],
                    stage=self.model_pusher_config.production_model_stage,
                    archive_existing_versions=self.model_pusher_config.archive_existing_versions,
                )

            elif (
                dic["accepted_model_info"] is not None
                and dic["prod_model_info"] is not None
            ):
                logging.info(
                    "Accepted model info is not None and Production model info is not None. Moving accepted model to production and production model to staging"
                )

                self.mlflow_client.transition_model_version_stage(
                    name=dic["accepted_model_info"]["model_name"],
                    version=dic["accepted_model_info"]["model_version"],
                    stage=self.model_pusher_config.production_model_stage,
                    archive_existing_versions=self.model_pusher_config.archive_existing_versions,
                )

                self.mlflow_client.transition_model_version_stage(
                    name=dic["prod_model_info"]["model_name"],
                    version=dic["prod_model_info"]["model_version"],
                    stage=self.model_pusher_config.staging_model_stage,
                    archive_existing_versions=self.model_pusher_config.archive_existing_versions,
                )

            else:
                logging.info("something went wrong")

                raise Exception("Something went wrong")

            logging.info("Exited initiate_model_pusher method of ModelPusher class")

        except Exception as e:
            raise CustomException(e, sys)
