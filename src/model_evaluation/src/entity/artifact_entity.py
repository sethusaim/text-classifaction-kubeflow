import os
from dataclasses import dataclass

from src.constant import training_pipeline


class ModelTrainerArtifact:
    def __init__(self, timestamp):
        self.model_training_dir: str = os.path.join(
            training_pipeline.ARTIFACT_DIR,
            timestamp,
            training_pipeline.MODEL_TRAINING_DIR,
        )

        self.model_training_best_model_info: str = os.path.join(
            self.model_training_dir, training_pipeline.MODEL_TRAINING_BEST_MODEL_INFO
        )

        self.model_training_best_model_path: str = os.path.join(
            self.model_training_dir, training_pipeline.MODEL_TRAINING_BEST_MODEL
        )


class DataTransformationArtifact:
    def __init__(self, timestamp):
        self.data_transformation_dir: str = os.path.join(
            training_pipeline.ARTIFACT_DIR,
            timestamp,
            training_pipeline.DATA_TRANSFORMATION_DIR,
            training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DIR,
        )

        self.transformed_test_features: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.DATA_TRANSFORMATION_TEST_FEATURES,
        )

        self.transformed_test_targets: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.DATA_TRANSFORMATION_TEST_TARGETS,
        )


@dataclass
class ClassifactionMetricArtifact:
    accuracy_score: float


@dataclass
class ModelEvaluationArtifact:
    is_model_accepted: bool

    best_model_path: str

    trained_model_path: str
