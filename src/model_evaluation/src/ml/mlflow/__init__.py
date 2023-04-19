import os
import sys
from typing import List, Tuple, Union

import mlflow

from src.configuration.mlflow_connection import MLFlowClient
from src.constant import training_pipeline
from src.entity.config_entity import MLFlowModelInfo
from src.exception import CustomException
from src.logger import logging


class MLFLowOperation:
    def __init__(self):
        self.mlflow_client = MLFlowClient().client

        mlflow.set_tracking_uri(uri=self.mlflow_client.tracking_uri)

        mlflow.set_experiment(experiment_name=training_pipeline.EXP_NAME)

    def get_model_info(self, best_model_path: str) -> MLFlowModelInfo:
        """
        This function retrieves information about a trained MLFlow model from a specified path.

        Args:
          best_model_path (str): A string representing the path to the directory containing the best
        trained model.

        Returns:
          an instance of the MLFlowModelInfo class.
        """
        logging.info("Entered get_model_info method of MLFLowOperation class")

        try:
            best_model_name: str = os.listdir(best_model_path)[0].split(".")[0]

            trained_best_model_info: Tuple[str, str, str, str] = [
                (
                    rm.name,
                    rm.latest_versions[0].current_stage,
                    rm.latest_versions[0].source,
                    rm.latest_versions[0].version,
                )
                for rm in self.mlflow_client.search_registered_models(
                    f"name='{best_model_name}'"
                )
            ][0]

            logging.info(
                f"Got a trained model info from registered models with filter name as {best_model_name}"
            )

            model_info: MLFlowModelInfo = MLFlowModelInfo(
                model_name=trained_best_model_info[0],
                model_current_stage=trained_best_model_info[1],
                model_uri=trained_best_model_info[2],
                model_version=trained_best_model_info[3],
            )

            logging.info(f"Created {model_info} model info dict")

            logging.info("Exited get_model_info method of MLFLowOperation class")

            return model_info

        except Exception as e:
            raise CustomException(e, sys)

    def get_prod_model_info(self) -> Union[MLFlowModelInfo, None]:
        """
        This function retrieves information about the latest production model from a list of registered
        models using the MLFlow API.

        Returns:
          an instance of the MLFlowModelInfo class or None.
        """
        logging.info("Entered get_prod_model_info method of MLFLowOperation class")

        try:
            prod_model_info: Union[List[Tuple[str, str, str, str]], None] = [
                (
                    rm.name,
                    rm.latest_versions[0].current_stage,
                    rm.latest_versions[0].source,
                    rm.latest_versions[0].version,
                )
                for rm in self.mlflow_client.search_registered_models()
                if rm.latest_versions[0].current_stage == "Production"
            ]

            logging.info(
                "got prod model info from list of registered models where current stage as Production"
            )

            if len(prod_model_info) == 0:
                logging.info("no prod model exists, trained model is accepted")

                return None

            else:
                prod_model_info: MLFlowModelInfo = MLFlowModelInfo(
                    model_name=prod_model_info[0][0],
                    model_current_stage=prod_model_info[0][1],
                    model_uri=prod_model_info[0][2],
                    model_version=prod_model_info[0][3],
                )

                return prod_model_info

        except Exception as e:
            raise CustomException(e, sys)
