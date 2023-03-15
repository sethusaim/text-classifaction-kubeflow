import sys

from src.cloud_storage.aws_storage import S3Operation
from src.entity.artifact_entity import ModelEvaluationArtifact, ModelTrainerArtifact
from src.entity.config_entity import ModelPusherConfig
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import read_json


class ModelPusher:
    def __init__(self, timestamp):
        self.model_trainer_artifact: ModelTrainerArtifact = ModelTrainerArtifact(
            timestamp=timestamp
        )

        self.model_evaluation_artifact: ModelEvaluationArtifact = (
            ModelEvaluationArtifact(timestamp=timestamp)
        )

        self.s3 = S3Operation()

        self.model_pusher_config: ModelPusherConfig = ModelPusherConfig()

    def initiate_model_pusher(self):
        logging.info("Entered initiate_model_pusher method of ModelPusher class")

        try:
            dic = read_json(
                file_path=self.model_evaluation_artifact.model_evaluation_info
            )

            if dic["is_model_accepted"] is True:
                logging.info("Trained model is accepted")

                self.s3.upload_file(
                    file_name=dic["trained_model_path"],
                    bucket_name=self.model_pusher_config.model_pusher_bucket_name,
                    bucket_file_name=self.model_pusher_config.model_pusher_bucket_file_name,
                )

            else:
                logging.info("Trained Model is not accepted")

                raise Exception("Trained Model is not accepted")

            logging.info("Exited initiate_model_pusher method of ModelPusher class")

        except Exception as e:
            raise CustomException(e, sys)
