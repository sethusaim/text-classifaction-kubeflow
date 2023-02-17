import os
import sys

import yaml

from src.exception import EcomException


def read_yaml_file(file_path: str) -> dict:
    """
    It reads a yaml file and returns a dictionary

    Args:
      file_path (str): str - The path to the YAML file to read.

    Returns:
      A dictionary
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise EcomException(e, sys) from e


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    It creates a directory if it doesn't exist, and then writes the content to the file

    Args:
      file_path (str): The path to the file you want to write to.
      content (object): The content to be written to the file.
      replace (bool): bool = False. Defaults to False
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)

    except Exception as e:
        raise EcomException(e, sys)
