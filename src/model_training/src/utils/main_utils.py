import os
import pickle
import sys

import dill
from scipy import sparse

from src.exception import CustomException


def load_csr_matrix(file_path: str):
    """
    This function loads a compressed sparse row matrix from a file path and returns it, or raises a
    custom exception if an error occurs.

    Args:
      file_path (str): A string representing the file path of a compressed sparse row (CSR) matrix file.

    Returns:
      a sparse matrix object loaded from the file specified by the file_path parameter.
    """
    try:
        file_obj = sparse.load_npz(file_path)

        return file_obj

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path: str):
    """
    This function loads an object from a file using the pickle module and raises a custom exception if
    there is an error.

    Args:
      file_path (str): A string representing the file path of the object to be loaded. This function
    uses the Python pickle module to deserialize the object from the file. If the file cannot be opened
    or deserialized, a CustomException is raised with the original exception and the sys module.

    Returns:
      the object loaded from the file located at the given file path. If there is an exception, it
    raises a custom exception with the original exception and the sys module.
    """
    try:
        with open(file_path, "rb") as f:
            file_obj = pickle.load(f)

        return file_obj

    except Exception as e:
        raise CustomException(e, sys)


def save_object(obj, file_path: str):
    """
    This function saves an object to a file using the dill library and raises a custom exception if
    there is an error.

    Args:
      obj: The object that needs to be saved to a file.
      file_path (str): The file path is a string that specifies the location and name of the file where
    the object will be saved. It should include the file extension, such as ".pkl" or ".dat".
    """
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as f:
            dill.dump(obj, f)

    except Exception as e:
        raise CustomException(e, sys)
