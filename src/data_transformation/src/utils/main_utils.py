import pickle
import sys

from scipy import sparse

from src.exception import EcomException


def save_csr_matrix(matrix, file_path: str):
    try:
        sparse.save_npz(file_path, matrix)

    except Exception as e:
        raise EcomException(e, sys)


def save_object(file_name, obj):
    try:
        with open(file_name, "wb") as f:
            pickle.dump(obj, f)

    except Exception as e:
        raise EcomException(e, sys)
