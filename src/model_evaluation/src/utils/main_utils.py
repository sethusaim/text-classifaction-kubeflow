import sys

import dill
from scipy import sparse

from src.exception import CustomException


def load_object(file_path: str):
    try:
        with open(file=file_path, mode="rb") as f:
            obj = dill.load(f)

        return obj

    except Exception as e:
        raise CustomException(e, sys)


def load_csr_matrix(file_path: str):
    try:
        file_obj = sparse.load_npz(file_path)

        return file_obj

    except Exception as e:
        raise CustomException(e, sys)
