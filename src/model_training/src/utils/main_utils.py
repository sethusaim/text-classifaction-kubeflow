import os
import pickle
import sys

import dill
from scipy import sparse

from src.exception import CustomException


def load_csr_matrix(file_path: str):
    try:
        file_obj = sparse.load_npz(file_path)

        return file_obj

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path: str):
    try:
        with open(file_path, "rb") as f:
            file_obj = pickle.load(f)

        return file_obj

    except Exception as e:
        raise CustomException(e, sys)


def save_object(obj, file_path: str):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as f:
            dill.dump(obj, f)

    except Exception as e:
        raise CustomException(e, sys)
