import os
import sys

import boto3

from src.exception import EcomException
from src.logger import logging


class S3Operation:
    def sync_folder_to_s3(
        self, folder: str, bucket_name: str, bucket_folder_name: str
    ) -> None:
        logging.info("Entered sync_folder_to_s3 method of S3Operation class")

        try:
            os.system(f"aws s3 sync {folder} s3://{bucket_name}/{bucket_folder_name}/ ")

            logging.info("Exited sync_folder_to_s3 method of S3Operation class")

        except Exception as e:
            raise EcomException(e, sys)

    def sync_folder_from_s3(
        self, folder: str, bucket_name: str, bucket_folder_name: str
    ) -> None:
        logging.info("Entered sync_folder_from_s3 method of S3Operation class")

        try:
            os.system(f"aws s3 sync s3://{bucket_name}/{bucket_folder_name}/ {folder}")

            logging.info("Exited sync_folder_from_s3 method of S3Operation class")

        except Exception as e:
            raise EcomException(e, sys)

    def get_pipeline_artifacts(self, bucket_name: str) -> None:
        logging.info("Entered get_pipeline_artifacts method of S3Operation class")

        try:
            s3_client = boto3.client("s3")

            response = s3_client.list_objects_v2(
                Bucket=bucket_name, Prefix="artifacts/"
            )["Contents"]

            latest = max(response, key=lambda x: x["LastModified"])["Key"]

            artifacts_dir = "/".join(latest.split("/")[:2])

            logging.info("Got the artifacts dir")

            self.sync_folder_from_s3(
                folder=artifacts_dir,
                bucket_name=bucket_name,
                bucket_folder_name=artifacts_dir,
            )

            logging.info("Exited get_pipeline_artifacts method of S3Operation class")

            return artifacts_dir.split("/")[1]

        except Exception as e:
            raise EcomException(e, sys)
