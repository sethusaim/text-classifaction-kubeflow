import os
from dataclasses import dataclass

from src.constant import training_pipeline


class DataIngestionArtifact:
    def __init__(self, timestamp):
        self.train_file_path: str = os.path.join(
            training_pipeline.ARTIFACT_DIR,
            timestamp,
            training_pipeline.DATA_INGESTION_DIR_NAME,
            training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,
            training_pipeline.TRAIN_FILE_NAME,
        )

        self.test_file_path: str = os.path.join(
            training_pipeline.ARTIFACT_DIR,
            timestamp,
            training_pipeline.DATA_INGESTION_DIR_NAME,
            training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,
            training_pipeline.TEST_FILE_NAME,
        )


@dataclass
class DataValidationArtifact:
    validation_status: bool

    valid_train_file_path: str

    valid_test_file_path: str

    invalid_train_file_path: str

    invalid_test_file_path: str

    drift_report_file_path: str
