import os

from src.constant import training_pipeline


class TrainingPipelineConfig:
    def __init__(self):
        self.artifacts_dir: str = training_pipeline.ARTIFACT_DIR

        self.artifact_bucket_name: str = training_pipeline.ARTIFACTS_BUCKET_NAME


class DataTransformationConfig:
    def __init__(self, timestamp):
        self.data_transformation_dir: str = os.path.join(
            training_pipeline.ARTIFACT_DIR,
            timestamp,
            training_pipeline.DATA_TRANSFORMATION_DIR,
            training_pipeline.DATA_TRANSFORMED_TRANSFORMED_DIR,
        )

        self.data_transformation_train_file_path: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.DATA_TRANSFORMATION_TRAIN_FILE_NAME,
        )

        self.config_folder: str = training_pipeline.DATA_TRANSFORMATION_CONFIG_FOLDER

        self.data_transformation_config_folder: str = os.path.join(
            training_pipeline.ARTIFACT_DIR,
            timestamp,
            training_pipeline.DATA_TRANSFORMATION_DIR,
            training_pipeline.DATA_TRANSFORMATION_CONFIG_FOLDER,
        )

        self.data_transformation_config_bucket_name: str = (
            training_pipeline.DATA_TRANSFORMATION_CONFIG_BUCKET_NAME
        )

        self.data_transformation_acronyms_file_path: str = os.path.join(
            self.data_transformation_config_folder,
            training_pipeline.DATA_TRANSFORMATION_ACRONYMS_CONFIG_FILE,
        )

        self.data_transformation_contraction_file_path: str = os.path.join(
            self.data_transformation_config_folder,
            training_pipeline.DATA_TRANSFORMATION_CONTRACTIONS_CONFIG_FILE,
        )

        self.transformed_train_features_file_path: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.TRANSFORMED_FEATURES_TRAIN_FILE,
        )

        self.transformed_val_features_file_path: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.TRANSFORMED_FEATURES_VAL_FILE,
        )

        self.transformed_test_features_file_path: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.TRANSFORMED_FEATURES_TEST_FILE,
        )

        self.transformed_train_targets_file_path: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.TRANSFORMED_TARGETS_TRAIN_FILE,
        )

        self.transformed_val_targets_file_path: str = os.path.join(
            self.data_transformation_dir, training_pipeline.TRANSFORMED_TARGETS_VAL_FILE
        )

        self.transformed_test_targets_file_path: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.TRANSFORMED_TARGETS_TEST_FILE,
        )

        self.transformed_vectorizer_file_path: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.TRANSFORMED_VECTORIZED_FILE_PATH,
        )
