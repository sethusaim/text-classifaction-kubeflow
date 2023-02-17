import sys

from src.cloud_storage.aws_operation import S3Operation
from src.exception import EcomException
from src.components.data_transformation import DataTransformation

s3 = S3Operation()


def start_data_validation():
    try:
        timestamp = s3.get_pipeline_artifacts(bucket_name="15787ecom-artifacts")

        data_transformation = DataTransformation(timestamp)

        data_transformation.initiate_data_transformation()

    except Exception as e:
        raise EcomException(e, sys)


if __name__ == "__main__":
    start_data_validation()
