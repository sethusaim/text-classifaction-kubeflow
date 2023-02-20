import sys

from src.components.data_validation import DataValidation
from src.exception import EcomException
from src.cloud_storage.aws_operations import S3Operation
from src.constant.training_pipeline import ARTIFACTS_BUCKET_NAME
from src.entity.config_entity import TrainingPipelineConfig

s3 = S3Operation()


def start_data_validation():
    try:
        timestamp = s3.get_pipeline_artifacts(bucket_name=ARTIFACTS_BUCKET_NAME)

        data_validation = DataValidation(timestamp)

        data_validation.initiate_data_validation()

    except Exception as e:
        raise EcomException(e, sys)

    finally:
        tp = TrainingPipelineConfig()

        s3.sync_folder_to_s3(
            folder=tp.artifact_dir,
            bucket_folder_name=tp.artifact_dir,
            bucket_name=tp.artifact_bucket_name,
        )


if __name__ == "__main__":
    start_data_validation()
