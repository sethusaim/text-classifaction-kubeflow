import os
import sys
from typing import List

import boto3

from src.exception import EcomException
from src.logger import logging


class S3Operation:
    def __init__(self):
        self.s3_client = boto3.client("s3")

        self.s3_resource = boto3.resource("s3")

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

    def get_pipeline_artifacts(self, bucket_name: str, folders: List) -> str:
        logging.info("Entered get_pipeline_artifacts method of S3Operation class")

        try:
            response = self.s3_client.list_objects_v2(
                Bucket=bucket_name, Prefix="artifacts"
            )["Contents"]

            latest = max(response, key=lambda x: x["LastModified"])["Key"]

            timestamp_artifact_dir = "/".join(latest.split("/")[:2])

            for f in folders:
                artifact_dir = timestamp_artifact_dir + "/" + f

                logging.info(f"Got the {f} artifacts dir")

                self.sync_folder_from_s3(
                    folder=artifact_dir,
                    bucket_name=bucket_name,
                    bucket_folder_name=artifact_dir,
                )

            logging.info("Exited get_pipeline_artifacts method of S3Operation class")

            return artifact_dir.split("/")[1]

        except Exception as e:
            raise EcomException(e, sys)

    def upload_file(self, file_name, bucket_name, bucket_file_name) -> None:
        logging.info("Entered upload_file method of S3Operation class")

        try:
            self.s3_resource.meta.client.upload_file(
                file_name, bucket_name, bucket_file_name
            )

            logging.info("Exited upload_file method of S3Operation class")

        except Exception as e:
            raise EcomException(e, sys)
