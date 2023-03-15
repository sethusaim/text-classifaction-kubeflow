import os

from src.constant import training_pipeline


class TrainingPipelineConfig:
    def __init__(self):
        self.artifacts_dir: str = training_pipeline.ARTIFACT_DIR

        self.artifact_bucket_name: str = training_pipeline.ARTIFACTS_BUCKET_NAME


class ModelTrainerConfig:
    def __init__(self, timestamp):
        self.model_training_dir: str = os.path.join(
            training_pipeline.ARTIFACT_DIR,
            timestamp,
            training_pipeline.MODEL_TRAINING_DIR,
        )

        self.expected_accuracy: float = training_pipeline.MODEL_TRAINER_EXCEPTED_SCORE

        self.model_trainer_config_file_path: str = (
            training_pipeline.MODEL_TRAINER_CONFIG_FILE_PATH
        )

        self.model_trainer_model_file_path: str = os.path.join(
            self.model_training_dir, training_pipeline.MODEL_TRAINER_MODEL_FILE_PATH
        )

        self.model_trainer_best_model_info_path: str = os.path.join(
            self.model_training_dir, training_pipeline.MODEL_TRAINER_BEST_MODEL_INFO
        )
