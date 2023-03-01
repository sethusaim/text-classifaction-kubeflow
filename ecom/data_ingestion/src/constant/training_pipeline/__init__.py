from datetime import datetime

TIMESTAMP: datetime = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

MONGODB_URL_KEY: str = "MONGO_DB_URL"

PIPELINE_NAME: str = "ecom"

ARTIFACT_DIR: str = "artifacts"

LOG_DIR: str = "logs"

APP_ARTIFACTS_BUCKET: str = "3998ecom-artifacts"

DATABASE_NAME: str = "ineuron"

TARGET_COLUMN: str = "class"

FILE_NAME: str = "ecom.csv"

TRAIN_FILE_NAME: str = "ecom_train.csv"

TEST_FILE_NAME: str = "ecom_test.csv"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "ecom"

DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_INGESTION_INGESTED_DIR: str = "ingested"

DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2
