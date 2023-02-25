import os
from src.constant import training_pipeline
from dataclasses import dataclass


class DataTransformationArtifact:
    def __init__(self, timestamp):
        self.data_transformation_dir: str = os.path.join(
            training_pipeline.ARTIFACT_DIR,
            timestamp,
            training_pipeline.DATA_TRANSFORMATION_DIR,
            training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DIR,
        )

        self.transformed_train_features: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.DATA_TRANSFORMATION_TRAIN_FEATURES,
        )

        self.transformed_val_features: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.DATA_TRANSFORMATION_VAL_FEATURES,
        )

        self.transformed_train_targets: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.DATA_TRANSFORMATION_TRAIN_TARGETS,
        )

        self.transformed_val_targets: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.DATA_TRANSFORMATION_VAL_TARGETS,
        )


@dataclass
class ClassifactionMetricArtifact:
    accuracy_score: float


@dataclass
class ModelInfoArtifact:
    model_name: str

    model_score: ClassifactionMetricArtifact

    model_parameters: dict
