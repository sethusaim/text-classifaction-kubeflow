import os

from src.constant import training_pipeline


class DataValidationArtifact:
    def __init__(self, timestamp):
        self.data_validation_dir: str = os.path.join(
            training_pipeline.ARTIFACT_DIR,
            timestamp,
            training_pipeline.DATA_VALIDATION_DIR,
            training_pipeline.DATA_VALIDATION_VALIDATED_DIR,
        )

        self.valid_train_file_path: str = os.path.join(
            self.data_validation_dir, training_pipeline.DATA_VALIDATION_TRAIN_FILE_NAME
        )

        self.valid_test_file_path: str = os.path.join(
            self.data_validation_dir, training_pipeline.DATA_VALIDATION_TEST_FILE_NAME
        )
