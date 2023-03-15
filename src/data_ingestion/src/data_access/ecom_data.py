import sys
from typing import Optional

import pandas as pd

from src.configuration.mongo_db_connection import MongoDBClient
from src.constant.training_pipeline import DATABASE_NAME
from src.exception import EcomException


class EcomData:
    def __init__(self):
        try:
            self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)

        except Exception as e:
            raise EcomException(e, sys)

    def export_collection_as_dataframe(
        self, collection_name: str, database_name: Optional[str] = None
    ) -> pd.DataFrame:
        """
        > This function takes in a collection name and database name (optional) and returns a pandas
        dataframe of the collection

        Args:
          collection_name (str): The name of the collection you want to export.
          database_name (Optional[str]): The name of the database you want to connect to.

        Returns:
          A dataframe
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
            raise EcomException(e, sys)
