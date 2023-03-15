import os

ARTIFACT_DIR: str = "artifacts"

ARTIFACTS_BUCKET_NAME: str = "41644ecom-artifacts"

SCHEMA_FILE_PATH: str = os.path.join("config", "schema.yaml")

TRAIN_FILE_NAME: str = "ecom_train.csv"

TEST_FILE_NAME: str = "ecom_test.csv"

# Data Ingestion
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2


## Data Validation
DATA_VALIDATION_DIR_NAME: str = "data_validation"

DATA_VALIDATION_VALID_DIR: str = "validated"

DATA_VALIDATION_INVALID_DIR: str = "invalid"

DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"

DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"
