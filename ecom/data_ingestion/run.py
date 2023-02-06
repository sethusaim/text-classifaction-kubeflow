# import sys

# from src.components.data_ingestion import DataIngestion
# from src.entity.artifact_entity import DataIngestionArtifact
# from src.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
# from src.exception import EcomException
# from src.cloud_storage.aws_operation import S3Sync

# s3 = S3Sync()

# training_pipeline_config = TrainingPipelineConfig()


# def start_data_ingestion() -> DataIngestionArtifact:
#     try:
#         data_ingestion_config = DataIngestionConfig(training_pipeline_config)

#         data_ingestion: DataIngestion = DataIngestion(data_ingestion_config)

#         data_ingestion.initiate_data_ingestion()

#     except Exception as e:
#         raise EcomException(e, sys)

#     finally:
#         s3 = S3Sync()

#         s3.sync_folder_to_s3(
#             folder=training_pipeline_config.artifact_dir,
#             bucket_name=training_pipeline_config.artifact_bucket_name,
#             bucket_folder_name=training_pipeline_config.artifact_dir,
#         )


# if __name__ == "__main__":
#     start_data_ingestion()

import subprocess


def start():
    try:
        res = subprocess.run("aws s3 ls", capture_output=True, shell=True)

        print(res.stdout)

    except Exception as e:
        print(res.stderr)


if __name__ == "__main__":
    start()
