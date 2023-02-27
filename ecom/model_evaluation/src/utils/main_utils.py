import pickle
import sys

from src.exception import EcomException
from scipy import sparse


def load_object(file_path: str):
    try:
        with open(file_path, "rb") as f:
            file_obj = pickle.load(f)

        return file_obj

    except Exception as e:
        raise EcomException(e, sys)


def load_csr_matrix(file_path: str):
    try:
        file_obj = sparse.load_npz(file_path)

        return file_obj

    except Exception as e:
        raise EcomException(e, sys)
