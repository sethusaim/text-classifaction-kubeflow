import os
import sys

from src.exception import CustomException
from src.logger import logging


class S3Operation:
    def sync_folder_to_s3(
        self, folder: str, bucket_name: str, bucket_folder_name: str
    ) -> None:
        """
        The function syncs a local folder to an S3 bucket using the AWS CLI and logs the process.

        Args:
          folder (str): The local folder path that needs to be synced to S3.
          bucket_name (str): The name of the S3 bucket where the folder will be synced to.
          bucket_folder_name (str): The name of the folder in the S3 bucket where the contents of the local
        folder will be synced to.
        """
        logging.info("Entered sync_folder_to_s3 method of S3Operation class")

        try:
            os.system(f"aws s3 sync {folder} s3://{bucket_name}/{bucket_folder_name}/ ")

            logging.info(f"Synced {folder} to s3://{bucket_name}/{bucket_folder_name}/")

            logging.info("Exited sync_folder_to_s3 method of S3Operation class")

        except Exception as e:
            raise CustomException(e, sys)
