import os
import sys

import pandas as pd
from sklearn.model_selection import train_test_split

from src.data_access.ecom_data import EcomData
from src.entity.artifact_entity import DataIngestionArtifact
from src.entity.config_entity import DataIngestionConfig
from src.exception import EcomException
from src.logger import logging


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config: DataIngestionConfig = DataIngestionConfig()

        self.ecom_data = EcomData()

    def export_data_into_feature_store(self) -> pd.DataFrame:
        """
        It takes the data from the MongoDB database and exports it into the feature store

        Returns:
          A dataframe
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

            logging.info("Exported data from mongodb to feature store")

            logging.info(
                "Exited export_data_into_feature_store method of DataIngestion class"
            )

            dataframe.to_csv(self.data_ingestion_config.feature_store_file_path)

            return dataframe

        except Exception as e:
            raise EcomException(e, sys)

    def split_data_as_train_test(self, dataframe: pd.DataFrame) -> None:
        """
        Feature store dataset will be split into train and test file
        """

        try:
            train_set, test_set = train_test_split(
                dataframe, test_size=self.data_ingestion_config.train_test_split_ratio
            )

            logging.info("Performed train test split on the dataframe")

            logging.info(
                "Exited split_data_as_train_test method of Data_Ingestion class"
            )

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

        except Exception as e:
            raise EcomException(e, sys)

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        """
        It takes a dataframe, converts it to a csv file and returns the path of the csv file

        Returns:
          DataIngestionArtifact
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
            raise EcomException(e, sys)
