import sys

import dill

from src.exception import CustomException


def load_object(file_path: str):
    """
    This function loads an object from a file using the dill library and raises a custom exception if
    there is an error.

    Args:
      file_path (str): The file path parameter is a string that represents the path to the file that
    contains the object to be loaded.

    Returns:
      an object that is loaded from a file using the dill library. The type and content of the object
    will depend on what was saved in the file. If there is an error during the loading process, a
    CustomException will be raised with the original error message and the sys module.
    """
    try:
        with open(file=file_path, mode="rb") as f:
            obj = dill.load(f)

        return obj

    except Exception as e:
        raise CustomException(e, sys)
