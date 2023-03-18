import os
import sys
from typing import Union


from src.cloud_storage.aws_storage import S3Operation
from src.exception import CustomException
from src.logger import logging

s3 = S3Operation()


def get_s3_model(model_path: str, bucket_name: str) -> Union[str, None]:
    try:
        model_dir: str = os.path.dirname(model_path)

        logging.info(f"Got model dir")

        if s3.is_model_present(model_path=model_path, bucket_name=bucket_name) is True:
            logging.info("Best model is present, downloading it")

            s3.sync_folder_from_s3(
                folder=model_dir,
                bucket_name=bucket_name,
                bucket_folder_name=model_dir,
            )

            logging.info("Downloaded best model from s3 bucket")

            return model_path

        else:
            logging.info("Best model not found in s3 bucket")

            return None

    except Exception as e:
        raise CustomException(e, sys)


class CustomModel:
    def __init__(self, preprocessor, model):
        try:
            self.preprocessor = preprocessor

            self.model = model

        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, x):
        try:
            x_transform = self.preprocessor.transform(x)

            y_hat = self.model.predict(x_transform)

            return y_hat

        except Exception as e:
            raise CustomException(e, sys)
