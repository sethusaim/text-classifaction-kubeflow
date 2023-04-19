import os
import sys

import pandas as pd

from src.cloud_storage.aws_operations import S3Operation
from src.constant.training_pipeline import SCHEMA_FILE_PATH
from src.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from src.entity.config_entity import DataValidationConfig
from src.exception import CustomException
from src.logger import logging
from src.utils.main_utils import read_yaml_file


class DataValidation:
    def __init__(self, timestamp):
        self.data_ingestion_artifact: DataIngestionArtifact = DataIngestionArtifact(
            timestamp
        )

        self.data_validation_config: DataValidationConfig = DataValidationConfig(
            timestamp
        )

        self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)

        self.s3 = S3Operation()

    def validate_number_of_columns(self, dataframe: pd.DataFrame) -> bool:
        """
        This function validates if the number of columns in a given dataframe matches the required number of
        columns specified in the schema configuration.

        Args:
          dataframe (pd.DataFrame): A pandas DataFrame that needs to be validated for the number of columns
        it has.

        Returns:
          a boolean value. It returns True if the number of columns in the input dataframe matches the
        number of columns specified in the schema configuration, and False otherwise.
        """
        try:
            number_of_columns = len(self._schema_config["columns"])

            logging.info(f"Required number of columns: {number_of_columns}")

            logging.info(f"Data frame has columns: {len(dataframe.columns)}")

            if len(dataframe.columns) == number_of_columns:
                return True

            return False

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        """
        This function initiates data validation by checking if the train and test dataframes contain all
        columns and saves the valid dataframes to specified directories.

        Returns:
          a DataValidationArtifact object.
        """
        try:
            os.makedirs(self.data_validation_config.valid_data_dir, exist_ok=True)

            os.makedirs(self.data_validation_config.invalid_data_dir, exist_ok=True)

            error_message = ""

            # Reading data from train and test file location
            train_dataframe = pd.read_csv(self.data_ingestion_artifact.train_file_path)

            test_dataframe = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            # Validate number of columns
            status = self.validate_number_of_columns(dataframe=train_dataframe)

            if not status:
                error_message = (
                    f"{error_message}Train dataframe does not contain all columns.\n"
                )

            status = self.validate_number_of_columns(dataframe=test_dataframe)

            if not status:
                error_message = (
                    f"{error_message}Test dataframe does not contain all columns.\n"
                )

            if not status:
                error_message = f"{error_message}Test dataframe does not contain all numerical columns.\n"

            if len(error_message) > 0:
                raise Exception(error_message)

            train_dataframe.to_csv(
                self.data_validation_config.valid_train_file_path,
                index=False,
                header=True,
            )

            test_dataframe.to_csv(
                self.data_validation_config.valid_test_file_path,
                index=False,
                header=True,
            )

            data_validation_artifact = DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=self.data_validation_config.valid_train_file_path,
                valid_test_file_path=self.data_validation_config.valid_test_file_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
                drift_report_file_path=self.data_validation_config.drift_report_file_path,
            )

            logging.info(f"Data validation artifact: {data_validation_artifact}")

            return data_validation_artifact

        except Exception as e:
            raise CustomException(e, sys)
