import sys

from src.exception import EcomException
from src.cloud_storage.aws_storage import S3Operation
from src.entity.config_entity import TrainingPipelineConfig
from src.components.model_evaluation import ModelEvaluation

s3 = S3Operation()

tp = TrainingPipelineConfig()


def start_model_evaluation():
    try:
        timestamp = s3.get_pipeline_artifacts(
            bucket_name=tp.artifact_bucket_name,
            folders=["model_training", "data_transformation"],
        )

        model_evaluation = ModelEvaluation(timestamp=timestamp)

        model_evaluation.initiate_model_evaluation()

    except Exception as e:
        raise EcomException(e, sys)

    finally:
        s3.sync_folder_to_s3(
            folder=tp.artifacts_dir,
            bucket_name=tp.artifact_bucket_name,
            bucket_folder_name=tp.artifacts_dir,
        )


if __name__ == "__main__":
    start_model_evaluation()
