import os
from dataclasses import dataclass
from typing import Dict

from src.constant import training_pipeline


class TrainingPipelineConfig:
    def __init__(self):
        self.artifacts_dir: str = training_pipeline.ARTIFACT_DIR

        self.artifact_bucket_name: str = training_pipeline.ARTIFACTS_BUCKET_NAME


class ModelEvaluationConfig:
    def __init__(self, timestamp):
        self.min_absolute_change: float = (
            training_pipeline.MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE
        )

        self.model_eval_threshold: float = training_pipeline.MODEL_EVALUATION_THRESHOLD

        self.higher_is_better: bool = True

        self.model_type: str = training_pipeline.MODEL_EVALUATION_MODEL_TYPE

        self.model_evaluation_dir: str = os.path.join(
            training_pipeline.ARTIFACT_DIR,
            timestamp,
            training_pipeline.MODEL_EVALUATION_DIR,
        )

        self.model_evaluation_info: str = os.path.join(
            self.model_evaluation_dir, training_pipeline.MODEL_EVALUATION_RESULT
        )


@dataclass
class MLFlowModelInfo:
    model_name: str

    model_current_stage: str

    model_uri: str

    model_version: str


@dataclass
class EvaluationModelResponse:
    is_model_accepted: bool

    trained_model_info: Dict

    accepted_model_info: Dict

    prod_model_info: Dict
