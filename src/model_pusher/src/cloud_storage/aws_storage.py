import os
import sys
from typing import List

import boto3

from src.exception import CustomException
from src.logger import logging


class S3Operation:
    def __init__(self):
        self.s3_client = boto3.client("s3")

        self.s3_resource = boto3.resource("s3")

    def sync_folder_to_s3(
        self, folder: str, bucket_name: str, bucket_folder_name: str
    ) -> None:
        """
        The function syncs a local folder to an S3 bucket using the AWS CLI.

        Args:
          folder (str): The local folder path that needs to be synced to S3 bucket.
          bucket_name (str): The name of the S3 bucket where the folder will be synced to.
          bucket_folder_name (str): The name of the folder in the S3 bucket where the contents of the local
        folder will be synced to.
        """
        logging.info("Entered sync_folder_to_s3 method of S3Operation class")

        try:
            os.system(f"aws s3 sync {folder} s3://{bucket_name}/{bucket_folder_name}/ ")

            logging.info("Exited sync_folder_to_s3 method of S3Operation class")

        except Exception as e:
            raise CustomException(e, sys)

    def sync_folder_from_s3(
        self, folder: str, bucket_name: str, bucket_folder_name: str
    ) -> None:
        """
        This Python function syncs a local folder with a folder in an S3 bucket using the AWS CLI.

        Args:
          folder (str): The local folder path where the files from S3 bucket will be synced to.
          bucket_name (str): The name of the S3 bucket from which the folder needs to be synced.
          bucket_folder_name (str): The name of the folder within the S3 bucket that needs to be synced with
        the local folder.
        """
        logging.info("Entered sync_folder_from_s3 method of S3Operation class")

        try:
            os.system(f"aws s3 sync s3://{bucket_name}/{bucket_folder_name}/ {folder}")

            logging.info("Exited sync_folder_from_s3 method of S3Operation class")

        except Exception as e:
            raise CustomException(e, sys)

    def get_pipeline_artifacts(self, bucket_name: str, folders: List) -> str:
        """
        This function retrieves the latest artifacts from an S3 bucket and syncs them to a local folder.

        Args:
          bucket_name (str): The name of the S3 bucket where the artifacts are stored.
          folders (List): A list of folder names for which the artifacts need to be retrieved from the S3
        bucket.

        Returns:
          The method is returning the name of the top-level directory of the latest artifacts folder in the
        specified S3 bucket, after syncing the specified subfolders within that artifacts folder to the
        local file system.
        """
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
            raise CustomException(e, sys)

    def upload_file(self, file_name, bucket_name, bucket_file_name) -> None:
        """
        This function uploads a file to an S3 bucket using the AWS SDK for Python (Boto3).

        Args:
          file_name: The local file path and name of the file that needs to be uploaded to S3.
          bucket_name: The name of the S3 bucket where the file will be uploaded to.
          bucket_file_name: The name of the file that will be used in the S3 bucket.
        """
        logging.info("Entered upload_file method of S3Operation class")

        try:
            self.s3_resource.meta.client.upload_file(
                file_name, bucket_name, bucket_file_name
            )

            logging.info("Exited upload_file method of S3Operation class")

        except Exception as e:
            raise CustomException(e, sys)
