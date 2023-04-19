import pickle
import sys

from scipy import sparse

from src.exception import CustomException


def save_csr_matrix(matrix: sparse.csr_matrix, file_path: str):
    """
    This function saves a compressed sparse row matrix to a specified file path.

    Args:
      matrix: a sparse matrix in Compressed Sparse Row (CSR) format that needs to be saved to a file.
      file_path (str): A string representing the file path where the compressed sparse row (CSR) matrix
    will be saved.
    """
    try:
        sparse.save_npz(file_path, matrix)

    except Exception as e:
        raise CustomException(e, sys)


def save_object(file_name: str, obj: object):
    """
    This function saves an object to a file using the pickle module in Python.

    Args:
      file_name: The name of the file where the object will be saved.
      obj: The object that needs to be saved to a file. It can be any Python object that is serializable
    using the pickle module.
    """
    try:
        with open(file_name, "wb") as f:
            pickle.dump(obj, f)

    except Exception as e:
        raise CustomException(e, sys)
