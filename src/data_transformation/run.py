import sys

from src.cloud_storage.aws_operation import S3Operation
from src.components.data_transformation import DataTransformation
from src.entity.config_entity import TrainingPipelineConfig
from src.exception import EcomException

s3 = S3Operation()

tp = TrainingPipelineConfig()


def start_data_transformation():
    try:
        timestamp = s3.get_pipeline_artifacts(
            bucket_name=tp.artifact_bucket_name, folders=["data_validation"]
        )

        data_transformation = DataTransformation(timestamp=timestamp)

        data_transformation.initiate_data_transformation()

    except Exception as e:
        raise EcomException(e, sys)

    finally:
        s3.sync_folder_to_s3(
            folder=tp.artifacts_dir,
            bucket_folder_name=tp.artifacts_dir,
            bucket_name=tp.artifact_bucket_name,
        )


if __name__ == "__main__":
    start_data_transformation()
