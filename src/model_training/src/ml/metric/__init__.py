import sys

from sklearn.metrics import accuracy_score

from src.entity.artifact_entity import ClassificationMetricArtifact
from src.exception import CustomException


def calculate_metric(model, x, y) -> ClassificationMetricArtifact:
    """
    This function calculates the accuracy score of a classification model given input data and labels.

    Args:
      model: a machine learning model that has been trained on some data and is capable of making
    predictions on new data.
      x: The input data used for making predictions with the model.
      y: The parameter 'y' is the true target variable values for the input data 'x'. It is used to
    evaluate the performance of the model by comparing the predicted values with the true values.

    Returns:
      an instance of the `ClassificationMetricArtifact` class, which contains the accuracy score of the
    model's predictions on the input data.
    """
    try:
        yhat = model.predict(x)

        model_metric = ClassificationMetricArtifact(
            accuracy_score=accuracy_score(y, yhat)
        )

        return model_metric

    except Exception as e:
        raise CustomException(e, sys)
