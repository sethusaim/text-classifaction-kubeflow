import os

from kfp import Client
from kfp.compiler import Compiler
from kfp.components import load_component_from_file
from kfp.dsl import BaseOp, pipeline

from ecom.api.auth import get_istio_auth_session

# KUBEFLOW_ENDPOINT = os.environ["KUBEFLOW_ENDPOINT"]
# KUBEFLOW_USERNAME = os.environ["KUBEFLOW_USERNAME"]
# KUBEFLOW_PASSWORD = os.environ["KUBEFLOW_PASSWORD"]


# auth_session = get_istio_auth_session(
#     url=KUBEFLOW_ENDPOINT, username=KUBEFLOW_USERNAME, password=KUBEFLOW_PASSWORD
# )

data_ingestion = load_component_from_file("kfp_components/data_ingestion.yaml")

data_validation = load_component_from_file("kfp_components/data_validation.yaml")

data_transformation = load_component_from_file(
    "kfp_components/data_transformation.yaml"
)

model_training = load_component_from_file("kfp_components/model_training.yaml")


@pipeline(name="Train Pipeline")
def train_pipeline():
    task_1: BaseOp = data_ingestion()

    task_2: BaseOp = data_validation()

    task_2.after(task_1)

    # task_3: BaseOp = data_transformation()

    # task_3.after(task_2)

    # task_4: BaseOp = model_training()

    # task_4.after(task_3)


if __name__ == "__main__":
    Compiler().compile(
        pipeline_func=train_pipeline, package_path="training-pipeline.yaml"
    )

    # client = Client(
    #     host=f"{KUBEFLOW_ENDPOINT}/pipeline", cookies=auth_session["session_cookie"]
    # )

    # client.create_run_from_pipeline_func(
    #     pipeline_func=train_pipeline,
    #     arguments={},
    #     namespace="kubeflow-user-example-com",
    #     experiment_name="kube-s3-test",
    #     service_account="kube-s3-sa",
    # )
