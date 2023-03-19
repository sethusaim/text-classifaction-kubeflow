import os

from mlflow.client import MlflowClient


class MLFlowClient:
    client = None

    def __init__(self):
        if MLFlowClient.client == None:
            __mlflow_tracking_uri = os.getenv("MLFLOW_TRACKING_URI")

            if __mlflow_tracking_uri is None:
                raise Exception(
                    f"Environment variable: MLFLOW_TRACKING_URI is not set."
                )

            MLFlowClient.client = MlflowClient(tracking_uri=__mlflow_tracking_uri)

        self.client = MLFlowClient.client
