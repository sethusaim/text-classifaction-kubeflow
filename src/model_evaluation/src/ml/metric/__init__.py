import json
import sys

from sklearn.metrics import accuracy_score

from src.entity.artifact_entity import ClassifactionMetricArtifact
from src.exception import CustomException


def calculate_metric(model, x, y) -> ClassifactionMetricArtifact:
    try:
        yhat = model.predict([x])

        model_metric = ClassifactionMetricArtifact(
            accuracy_score=accuracy_score(y, yhat)
        )

        return model_metric

    except Exception as e:
        raise CustomException(e, sys)


def get_model_score(file_path: str):
    try:
        with open(file=file_path, mode="r") as f:
            dic = json.load(f)

        return dic["model_score"]["accuracy_score"]

    except Exception as e:
        raise CustomException(e, sys)
