import os
import sys
from typing import List

import boto3

from src.exception import CustomException
from src.logger import logging


class S3Operation:
    def __init__(self):
        self.s3_client = boto3.client("s3")

    def sync_folder_to_s3(
        self, folder: str, bucket_name: str, bucket_folder_name: str
    ) -> None:
        """
        This function syncs a local folder to an S3 bucket using the AWS CLI.

        Args:
          folder (str): The local folder path that you want to sync with the S3 bucket.
          bucket_name (str): The name of the S3 bucket where the folder will be synced to.
          bucket_folder_name (str): The name of the folder in the S3 bucket where the contents of the local
        folder will be synced to.
        """
        try:
            os.system(f"aws s3 sync {folder} s3://{bucket_name}/{bucket_folder_name}/ ")

        except Exception as e:
            raise CustomException(e, sys)

    def sync_folder_from_s3(
        self, folder: str, bucket_name: str, bucket_folder_name: str
    ) -> None:
        """
        This Python function syncs a local folder with a specified folder in an AWS S3 bucket.

        Args:
          folder (str): The local folder path where the files from the S3 bucket will be synced to.
          bucket_name (str): The name of the S3 bucket from which the folder needs to be synced.
          bucket_folder_name (str): The name of the folder within the S3 bucket that you want to sync with
        the local folder specified by the 'folder' parameter.
        """
        try:
            os.system(f"aws s3 sync s3://{bucket_name}/{bucket_folder_name}/ {folder} ")

        except Exception as e:
            raise CustomException(e, sys)

    def get_pipeline_artifacts(self, bucket_name: str, folders: List) -> str:
        """
        This function retrieves the latest artifacts from an S3 bucket and syncs them to a local folder.

        Args:
          bucket_name (str): The name of the S3 bucket where the artifacts are stored.
          folders (List): A list of folder names within the "artifacts" directory that need to be synced
        from the S3 bucket.

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
