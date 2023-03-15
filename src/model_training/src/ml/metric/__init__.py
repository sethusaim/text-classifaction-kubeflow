import sys

from sklearn.metrics import accuracy_score

from src.entity.artifact_entity import ClassifactionMetricArtifact
from src.exception import EcomException


def calculate_metric(model, x, y) -> ClassifactionMetricArtifact:
    try:
        yhat = model.predict(x)

        model_metric = ClassifactionMetricArtifact(
            accuracy_score=accuracy_score(y, yhat)
        )

        return model_metric

    except Exception as e:
        raise EcomException(e, sys)
