from src.constant import training_pipeline


class TrainingPipelineConfig:
    def __init__(self):
        self.artifacts_dir: str = training_pipeline.ARTIFACT_DIR

        self.artifacts_bucket_name: str = training_pipeline.ARTIFACTS_BUCKET_NAME


class ModelPusherConfig:
    def __init__(self):
        self.production_model_stage: str = (
            training_pipeline.MODEL_PUSHER_PROD_MODEL_STAGE
        )

        self.staging_model_stage: str = training_pipeline.MODEL_PUSHER_STAG_MODEL_STAGE

        self.archive_existing_versions: bool = (
            training_pipeline.MODEL_PUSHER_ARCHIVE_EXISTING_VERSIONS
        )
