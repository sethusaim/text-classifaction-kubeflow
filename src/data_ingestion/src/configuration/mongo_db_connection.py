import os
import sys

import certifi
from pymongo import MongoClient

from src.constant.training_pipeline import DATABASE_NAME, MONGODB_URL_KEY
from src.exception import CustomException

ca = certifi.where()


class MongoDBClient:
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY)

                if mongo_db_url is not None:
                    if "localhost" in mongo_db_url:
                        MongoDBClient.client = MongoClient(mongo_db_url)

                    else:
                        MongoDBClient.client = MongoClient(mongo_db_url, tlsCAFile=ca)

                else:
                    raise Exception(
                        f"{MONGODB_URL_KEY} environment variable is not set"
                    )

            self.client = MongoDBClient.client

            self.database = self.client[database_name]

            self.database_name = database_name

        except Exception as e:
            raise CustomException(e, sys)
