import os
from dataclasses import dataclass

from src.constant import training_pipeline
from src.entity.config_entity import MLFlowModelInfo


class ModelTrainerArtifact:
    def __init__(self, timestamp):
        self.model_training_dir: str = os.path.join(
            training_pipeline.ARTIFACT_DIR,
            timestamp,
            training_pipeline.MODEL_TRAINING_DIR,
        )

        self.model_training_best_model_dir: str = os.path.join(
            self.model_training_dir, training_pipeline.MODEL_TRAINING_BEST_MODEL_DIR
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
class ClassificationMetricArtifact:
    accuracy_score: float


@dataclass
class ModelEvaluationArtifact:
    is_model_accepted: bool

    trained_model_info: MLFlowModelInfo

    accepted_model_info: MLFlowModelInfo

    prod_model_info: MLFlowModelInfo
