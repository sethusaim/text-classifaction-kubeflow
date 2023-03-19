import sys

from src.exception import CustomException
from src.cloud_storage.aws_storage import S3Operation
from src.entity.config_entity import TrainingPipelineConfig
from src.components.model_pusher import ModelPusher

s3 = S3Operation()

tp = TrainingPipelineConfig()


def start_model_pusher():
    try:
        timestamp = s3.get_pipeline_artifacts(
            bucket_name=tp.artifacts_bucket_name,
            folders=["model_evaluation"],
        )

        model_pusher = ModelPusher(timestamp=timestamp)

        model_pusher.initiate_model_pusher()

    except Exception as e:
        raise CustomException(e, sys)


if __name__ == "__main__":
    start_model_pusher()
