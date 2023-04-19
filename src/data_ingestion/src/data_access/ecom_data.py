import sys
from typing import Optional

import pandas as pd

from src.configuration.mongo_db_connection import MongoDBClient
from src.constant.training_pipeline import DATABASE_NAME
from src.exception import CustomException


class EcomData:
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)

        except Exception as e:
            raise CustomException(e, sys)

    def export_collection_as_dataframe(
        self, collection_name: str, database_name: Optional[str] = None
    ) -> pd.DataFrame:
        """
        This function exports a MongoDB collection as a pandas DataFrame.

        Args:
          collection_name (str): The name of the MongoDB collection to export as a Pandas DataFrame.
          database_name (Optional[str]): Optional parameter that specifies the name of the database where
        the collection is located. If not provided, the method assumes that the collection is located in the
        default database of the MongoDB client.

        Returns:
          a pandas DataFrame containing the data from a MongoDB collection specified by the input parameters
        `collection_name` and `database_name` (optional). If the collection contains an `_id` field, it will
        be dropped from the DataFrame before returning it. If an exception occurs during the execution of
        the function, a custom exception will be raised with the error message and the `sys` module.
        """
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]

            else:
                collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))

            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)

            return df

        except Exception as e:
            raise CustomException(e, sys)
