import os

from kfp import Client
from kfp.components import load_component_from_file
from kfp.dsl import pipeline, BaseOp

from ecom.api.auth import get_istio_auth_session

KUBEFLOW_ENDPOINT = os.environ["KUBEFLOW_ENDPOINT"]
KUBEFLOW_USERNAME = os.environ["KUBEFLOW_USERNAME"]
KUBEFLOW_PASSWORD = os.environ["KUBEFLOW_PASSWORD"]


auth_session = get_istio_auth_session(
    url=KUBEFLOW_ENDPOINT, username=KUBEFLOW_USERNAME, password=KUBEFLOW_PASSWORD
)

data_ingestion = load_component_from_file("kfp_components/data_ingestion.yaml")


@pipeline(name="Train Pipeline")
def train_pipeline():
    task_1: BaseOp = data_ingestion()


if __name__ == "__main__":
    client = Client(
        host=f"{KUBEFLOW_ENDPOINT}/pipeline", cookies=auth_session["session_cookie"]
    )

    client.create_run_from_pipeline_func(
        pipeline_func=train_pipeline,
        arguments={},
        namespace="kubeflow-user-example-com",
        experiment_name="kube-s3-test",
        service_account="kube-s3-sa",
    )
