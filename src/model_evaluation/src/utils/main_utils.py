import sys

import dill

from src.exception import CustomException


def load_object(file_path: str):
    try:
        with open(file=file_path, mode="rb") as f:
            obj = dill.load(f)

        return obj

    except Exception as e:
        raise CustomException(e, sys)
