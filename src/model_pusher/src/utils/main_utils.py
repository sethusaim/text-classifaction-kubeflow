import sys

from src.exception import CustomException
import json


def read_json(file_path: str):
    try:
        with open(file=file_path, mode="r") as f:
            dic = json.load(f)

        return dic

    except Exception as e:
        raise CustomException(e, sys)
