import sys

from sklearn.metrics import accuracy_score

from src.entity.artifact_entity import ClassificationMetricArtifact
from src.exception import CustomException


def calculate_metric(model, x, y) -> ClassificationMetricArtifact:
    try:
        yhat = model.predict(x)

        model_metric = ClassificationMetricArtifact(
            accuracy_score=accuracy_score(y, yhat)
        )

        return model_metric

    except Exception as e:
        raise CustomException(e, sys)
