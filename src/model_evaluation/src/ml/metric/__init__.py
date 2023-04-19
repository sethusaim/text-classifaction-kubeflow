import json
import sys

from sklearn.metrics import accuracy_score

from src.entity.artifact_entity import ClassificationMetricArtifact
from src.exception import CustomException


def calculate_metric(model, x, y) -> ClassificationMetricArtifact:
    """
    This function calculates the accuracy score of a classification model given input data and labels.

    Args:
      model: The machine learning model that has been trained and is being used for prediction.
      x: The input data for the model to make predictions on. It could be a single data point or a batch
    of data points.
      y: The parameter 'y' is the true label or target value of the input data 'x'. It is used to
    evaluate the performance of the model by comparing the predicted output with the actual output.

    Returns:
      an instance of the `ClassificationMetricArtifact` class, which contains the accuracy score of the
    model's predictions on the input data `x` and `y`.
    """
    try:
        yhat = model.predict([x])

        model_metric = ClassificationMetricArtifact(
            accuracy_score=accuracy_score(y, yhat)
        )

        return model_metric

    except Exception as e:
        raise CustomException(e, sys)


def get_model_score(file_path: str):
    """
    This function reads a JSON file and returns the accuracy score of a model stored in the file, or
    raises a custom exception if there is an error.

    Args:
      file_path (str): A string representing the file path of a JSON file containing a dictionary with a
    "model_score" key and an "accuracy_score" sub-key. The function reads the file and returns the value
    of the "accuracy_score" sub-key. If there is an error reading the file or accessing the sub-key

    Returns:
      the accuracy score of a model, which is extracted from a JSON file located at the file path
    specified in the function argument. If there is an exception, a custom exception is raised with the
    original exception and the sys module.
    """
    try:
        with open(file=file_path, mode="r") as f:
            dic = json.load(f)

        return dic["model_score"]["accuracy_score"]

    except Exception as e:
        raise CustomException(e, sys)
