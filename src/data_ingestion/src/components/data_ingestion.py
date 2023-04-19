import os
import sys

import pandas as pd
from sklearn.model_selection import train_test_split

from src.data_access.ecom_data import EcomData
from src.entity.artifact_entity import DataIngestionArtifact
from src.entity.config_entity import DataIngestionConfig
from src.exception import CustomException
from src.logger import logging


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config: DataIngestionConfig = DataIngestionConfig()

        self.ecom_data = EcomData()

    def export_data_into_feature_store(self) -> pd.DataFrame:
        """
        This function exports data from MongoDB to a feature store and saves it as a CSV file.

        Returns:
          The method is returning a pandas DataFrame object.
        """
        logging.info(
            "Entered export_data_into_feature_store method of DataIngestion class"
        )

        try:
            logging.info("Exporting data from mongodb to feature store")

            os.makedirs(self.data_ingestion_config.feature_store_dir, exist_ok=True)

            dataframe: pd.DataFrame = self.ecom_data.export_collection_as_dataframe(
                collection_name=self.data_ingestion_config.collection_name
            )

            dataframe.to_csv(self.data_ingestion_config.feature_store_file_path)

            logging.info("Exported data from mongodb to feature store")

            logging.info(
                "Exited export_data_into_feature_store method of DataIngestion class"
            )

            return dataframe

        except Exception as e:
            raise CustomException(e, sys)

    def split_data_as_train_test(self, dataframe: pd.DataFrame) -> None:
        """
        This function splits a given dataframe into training and testing sets, saves them as CSV files, and
        logs the process.

        Args:
          dataframe (pd.DataFrame): A pandas DataFrame containing the data to be split into training and
        testing sets.
        """
        logging.info("Entered split_data_as_train_test method of Data_Ingestion class")

        try:
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio
            )

            logging.info("Performed train test split on the dataframe")

            dir_path: str = os.path.dirname(
                self.data_ingestion_config.training_file_path
            )

            os.makedirs(dir_path, exist_ok=True)

            logging.info(f"Exporting train and test file path.")

            train_set.to_csv(
                self.data_ingestion_config.training_file_path, index=False, header=True
            )

            test_set.to_csv(
                self.data_ingestion_config.testing_file_path, index=False, header=True
            )

            logging.info(f"Exported train and test file path.")

            logging.info(
                "Exited split_data_as_train_test method of Data_Ingestion class"
            )

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        This function initiates data ingestion by exporting data into a feature store, splitting the data
        into train and test sets, and returning a DataIngestionArtifact object.

        Returns:
          The method `initiate_data_ingestion` returns an instance of the `DataIngestionArtifact` class.
        """
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")

        try:
            dataframe: pd.DataFrame = self.export_data_into_feature_store()

            self.split_data_as_train_test(dataframe=dataframe)

            data_ingestion_artifact: DataIngestionArtifact = DataIngestionArtifact(
                feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            )

            logging.info(f"Data Ingestion artifact is : {data_ingestion_artifact}")

            logging.info("Exited initiate_data_ingestion method of DataIngestion class")

            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e, sys)
