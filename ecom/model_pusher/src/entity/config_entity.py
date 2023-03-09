from src.constant import training_pipeline


class TrainingPipelineConfig:
    def __init__(self):
        self.artifacts_dir: str = training_pipeline.ARTIFACT_DIR

        self.artifacts_bucket_name: str = training_pipeline.ARTIFACTS_BUCKET_NAME


class ModelPusherConfig:
    def __init__(self):
        self.model_pusher_bucket_name: str = (
            training_pipeline.MODEL_PUSHER_CONFIG_BUCKET
        )

        self.model_pusher_bucket_file_name: str = (
            training_pipeline.MODEL_PUSHER_BUCKET_MODEL_PATH
        )
