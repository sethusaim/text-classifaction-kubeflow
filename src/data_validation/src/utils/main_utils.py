import os
import sys
from typing import Dict

import yaml

from src.exception import CustomException


def read_yaml_file(file_path: str) -> Dict:
    """
    This function reads a YAML file from a given file path and returns its contents as a dictionary,
    raising a custom exception if there is an error.

    Args:
      file_path (str): The file path parameter is a string that represents the path to the YAML file
    that needs to be read.

    Returns:
      a dictionary object that is loaded from a YAML file located at the specified file path.
    """
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise CustomException(e, sys)


def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    """
    This function writes YAML content to a file path and can optionally replace an existing file.

    Args:
      file_path (str): A string representing the path to the YAML file that will be written.
      content (object): The content parameter is an object that will be written to a YAML file. It can
    be any Python object that can be serialized to YAML format.
      replace (bool): A boolean parameter that determines whether to replace an existing file with the
    same name or not. If set to True and a file with the same name already exists, it will be deleted
    before writing the new file. If set to False and a file with the same name already exists, an error
    will be. Defaults to False
    """
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "w") as file:
            yaml.dump(content, file)

    except Exception as e:
        raise CustomException(e, sys)
