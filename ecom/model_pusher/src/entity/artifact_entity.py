import os
from src.constant import training_pipeline


class ModelTrainerArtifact:
    def __init__(self, timestamp):
        self.model_trainer_dir: str = os.path.join(
            training_pipeline.ARTIFACT_DIR,
            timestamp,
            training_pipeline.MODEL_TRAINER_DIR,
        )

        self.model_trainer_model_info: str = os.path.join(
            self.model_trainer_dir, training_pipeline.MODEL_TRAINER_MODEL_INFO
        )

        self.model_trainer_model_path: str = os.path.join(
            self.model_trainer_dir, training_pipeline.MODEL_TRAINER_MODEL_PATH
        )


class ModelEvaluationArtifact:
    def __init__(self, timestamp):
        self.model_evaluation_dir: str = os.path.join(
            training_pipeline.ARTIFACT_DIR,
            timestamp,
            training_pipeline.MODEL_EVALUATION_DIR,
        )

        self.model_evaluation_info: str = os.path.join(
            self.model_evaluation_dir, training_pipeline.MODEL_EVALUATION_MODEL_INFO
        )
