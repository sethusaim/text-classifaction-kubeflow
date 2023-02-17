import sys

import pandas as pd

from src.exception import EcomException
from src.logger import logging
from src.constant.training_pipeline import LABEL_DICT


class DataTransformation:
    def __init__(self, timestamp):
        pass

    def drop_duplicate_and_null_records(self, data_frame: pd.DataFrame) -> pd.DataFrame:
        logging.info(
            "Entered drop_duplicate_records method of DataTransformation class"
        )

        try:
            df: pd.DataFrame = data_frame.drop_duplicates()

            logging.info("Dropped duplicate records in dataframe")

            df: pd.DataFrame = df.dropna()

            logging.info("Dropped na values from the dataframe")

            logging.info(
                "Exited drop_duplicate_records method of DataTransformation class"
            )

            return df

        except Exception as e:
            raise EcomException(e, sys)

    def encode_target_cols(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        logging.info("Entered encode_target_cols method of DataTransformation class")

        try:
            dataframe.replace({"label": LABEL_DICT}, inplace=True)

            logging.info("Encoded target columns with label dict")

            logging.info("Exited encode_target_cols method of DataTransformation class")

            return dataframe

        except Exception as e:
            raise EcomException(e, sys)

    def initiate_data_transformation(self):
        logging.info(
            "Entered initiate_data_transformation method of DataTransformation class"
        )

        try:
            df: pd.DataFrame = pd.read_csv(
                "artifacts/02_17_2023_14_23_24/data_validation/validated/ecom_train.csv"
            )

            df: pd.DataFrame = self.drop_duplicate_and_null_records(data_frame=df)

            df: pd.DataFrame = self.encode_target_cols(dataframe=df)

            df.to_csv("data_transformed.csv", index=False, header=True)

            logging.info(
                "Exited initiate_data_transformation method of DataTransformation class"
            )

        except Exception as e:
            raise EcomException(e, sys)
