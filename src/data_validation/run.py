import sys

from src.components.data_validation import DataValidation
from src.exception import CustomException
from src.cloud_storage.aws_operations import S3Operation
from src.entity.config_entity import TrainingPipelineConfig

s3 = S3Operation()

tp = TrainingPipelineConfig()


def start_data_validation():
    """
    This function initiates data validation using a timestamp obtained from an S3 bucket and catches any
    exceptions that may occur.
    """
    try:
        timestamp = s3.get_pipeline_artifacts(
            bucket_name=tp.artifact_bucket_name, folders=["data_ingestion"]
        )

        data_validation = DataValidation(timestamp)

        data_validation.initiate_data_validation()

    except Exception as e:
        raise CustomException(e, sys)

    finally:
        s3.sync_folder_to_s3(
            folder=tp.artifact_dir,
            bucket_folder_name=tp.artifact_dir,
            bucket_name=tp.artifact_bucket_name,
        )


if __name__ == "__main__":
    start_data_validation()
