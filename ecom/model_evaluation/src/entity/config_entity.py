import os

from src.constant import training_pipeline
from dataclasses import dataclass


class TrainingPipelineConfig:
    def __init__(self):
        self.artifacts_dir: str = training_pipeline.ARTIFACT_DIR

        self.artifact_bucket_name: str = training_pipeline.ARTIFACTS_BUCKET_NAME


class ModelEvaluationConfig:
    def __init__(self, timestamp):
        self.model_evaluation_dir: str = os.path.join(
            training_pipeline.ARTIFACT_DIR,
            timestamp,
            training_pipeline.MODEL_EVALUATION_DIR,
        )

        self.model_evaluation_s3_model_bucket: str = (
            training_pipeline.MODEL_EVALUATION_S3_MODEL_BUCKET
        )

        self.model_evaluation_s3_model_path: str = (
            training_pipeline.MODEL_EVALUATION_S3_MODEL_PATH
        )

        self.model_evaluation_info: str = os.path.join(
            self.model_evaluation_dir,
            training_pipeline.MODEL_EVALUATION_INFO,
        )


@dataclass
class EvaluationModelResponse:
    trained_model_score: float

    trained_model_path: str

    best_model_score: float

    best_model_path: str

    is_model_accepted: bool

    changed_score: float
