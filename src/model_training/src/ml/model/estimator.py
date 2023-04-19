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
        """
        This function takes in a context and a DataFrame, applies a preprocessor to the DataFrame, uses a
        model to make predictions, and returns the predictions.

        Args:
          context: The context parameter is a dictionary containing any additional information or context
        that may be needed for the prediction. This could include things like configuration settings, model
        hyperparameters, or other relevant information.
          dataframe (DataFrame): A pandas DataFrame containing the input data to be used for making
        predictions.

        Returns:
          The code is returning the predictions made by the model on the input data after transforming it
        using the preprocessor. The output is a DataFrame containing the predicted values.
        """
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
