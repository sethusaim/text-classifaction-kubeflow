import os
import sys
from typing import Union


from src.cloud_storage.aws_storage import S3Operation
from src.exception import CustomException
from src.logger import logging

s3 = S3Operation()


def get_s3_model(model_path: str, bucket_name: str) -> Union[str, None]:
    """
    This function checks if a model is present in an S3 bucket and downloads it if it is.

    Args:
      model_path (str): A string representing the path to the model file.
      bucket_name (str): The name of the S3 bucket where the model is stored.

    Returns:
      either a string representing the model path or None, depending on whether the best model is
    present in the specified S3 bucket.
    """
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
        """
        This function takes in an input, transforms it using a preprocessor, predicts an output using a
        model, and returns the predicted output.

        Args:
          x: The input data that needs to be predicted by the model.

        Returns:
          The function `predict` returns the predicted values `y_hat` for the input `x` after transforming
        it using the preprocessor and using the trained model to make the prediction. If an exception occurs
        during the prediction process, a `CustomException` is raised with the original exception and the
        `sys` module.
        """
        try:
            x_transform = self.preprocessor.transform(x)

            y_hat = self.model.predict(x_transform)

            return y_hat

        except Exception as e:
            raise CustomException(e, sys)
