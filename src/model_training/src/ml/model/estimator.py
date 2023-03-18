import sys

from mlflow.pyfunc import PythonModel
from pandas import DataFrame
from sklearn.pipeline import Pipeline

from src.exception import CustomException


class CustomModel(PythonModel):
    def __init__(self, preprocessor: Pipeline, model: object):
        self.preprocessor = preprocessor

        self.model = model

    def predict(self, context, dataframe: DataFrame) -> DataFrame:
        try:
            transformed_feature = self.preprocessor.transform(dataframe)

            preds = self.model.predict(transformed_feature)

            return preds

        except Exception as e:
            raise CustomException(e, sys)

    def __repr__(self):
        return f"{type(self.model).__name__}()"

    def __str__(self):
        return f"{type(self.model).__name__}()"
