import sys

from src.exception import CustomException
import json


def read_json(file_path: str):
    """
    This function reads a JSON file from a given file path and returns its contents as a dictionary,
    raising a custom exception if there is an error.

    Args:
      file_path (str): The file path parameter is a string that represents the path to the JSON file
    that needs to be read.

    Returns:
      a dictionary object that is loaded from a JSON file located at the file path specified in the
    input argument. If an exception occurs during the file reading or JSON decoding process, a custom
    exception is raised with the original exception and the system information.
    """
    try:
        with open(file=file_path, mode="r") as f:
            dic = json.load(f)

        return dic

    except Exception as e:
        raise CustomException(e, sys)
