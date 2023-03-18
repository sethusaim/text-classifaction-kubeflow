import os
import sys
from typing import Tuple

import pandas as pd
from scipy import sparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

from src.cloud_storage.aws_operation import S3Operation
from src.constant import training_pipeline
from src.constant.training_pipeline import LABEL_DICT
from src.entity.artifact_entity import (
    DataTransformationArtifact,
    DataValidationArtifact,
)
from src.entity.config_entity import DataTransformationConfig
from src.exception import CustomException
from src.logger import logging
from src.ml.feature import text_normalizer
from src.utils.main_utils import save_object


class DataTransformation:
    def __init__(self, timestamp):
        self.data_transformation_config: DataTransformationConfig = (
            DataTransformationConfig(timestamp=timestamp)
        )

        self.data_validation_artifact: DataValidationArtifact = DataValidationArtifact(
            timestamp
        )

        self.s3 = S3Operation()

    def drop_duplicate_and_null_records(self, data_frame: pd.DataFrame) -> pd.DataFrame:
        logging.info(
            "Entered drop_duplicate_records method of DataTransformation class"
        )

        try:
            df: pd.DataFrame = data_frame.drop_duplicates()

            logging.info("Dropped duplicate records in dataframe")

            df: pd.DataFrame = df.dropna()

            logging.info("Dropped na values from the dataframe")

            logging.info(
                "Exited drop_duplicate_records method of DataTransformation class"
            )

            return df

        except Exception as e:
            raise CustomException(e, sys)

    def encode_target_cols(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        logging.info("Entered encode_target_cols method of DataTransformation class")

        try:
            dataframe.replace({"label": LABEL_DICT}, inplace=True)

            logging.info("Encoded target columns with label dict")

            logging.info("Exited encode_target_cols method of DataTransformation class")

            return dataframe

        except Exception as e:
            raise CustomException(e, sys)

    def split_data(
        self, data_frame: pd.DataFrame
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        logging.info("Entered split_data method of DataTransformation class")

        try:
            X, y = (
                data_frame.drop(training_pipeline.TARGET_COL, axis=1),
                data_frame[training_pipeline.TARGET_COL],
            )

            logging.info("Created features and targets dataframe")

            X_train, X_test, y_train, y_test = train_test_split(
                X, y, **training_pipeline.SPLIT_KWARGS
            )

            logging.info("Performed train test split based on kwargs")

            data_train = pd.concat([X_train, y_train], axis=1)

            logging.info("Created training data")

            X_val, X_test, y_val, y_test = train_test_split(
                X_test, y_test, **training_pipeline.SPLIT_KWARGS
            )

            logging.info("Created validation and test dataframe")

            df_val = pd.concat([X_val, y_val], axis=1)

            df_test = pd.concat([X_test, y_test], axis=1)

            logging.info("Created validation and testing data")

            logging.info("Exited split_data method of DataTransformation class")

            return data_train, df_val, df_test

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self):
        logging.info(
            "Entered initiate_data_transformation method of DataTransformation class"
        )

        try:
            os.makedirs(
                self.data_transformation_config.data_transformation_dir, exist_ok=True
            )

            self.s3.sync_folder_from_s3(
                folder=self.data_transformation_config.data_transformation_config_folder,
                bucket_name=self.data_transformation_config.data_transformation_config_bucket_name,
                bucket_folder_name=self.data_transformation_config.config_folder,
            )

            logging.info("Got config files from s3")

            df: pd.DataFrame = pd.read_csv(
                self.data_validation_artifact.valid_train_file_path
            )

            df: pd.DataFrame = self.drop_duplicate_and_null_records(data_frame=df)

            df: pd.DataFrame = self.encode_target_cols(dataframe=df)

            acronyms_dict = pd.read_json(
                self.data_transformation_config.data_transformation_acronyms_file_path,
                typ="series",
            )

            logging.info("Got acronyms dict")

            contractions_dict = pd.read_json(
                self.data_transformation_config.data_transformation_contraction_file_path,
                typ="series",
            )

            logging.info("Got contractions dict")

            df_train, df_val, df_test = self.split_data(data_frame=df)

            data_train_norm, data_val_norm, data_test_norm = (
                pd.DataFrame(),
                pd.DataFrame(),
                pd.DataFrame(),
            )

            data_train_norm["normalized description"] = df_train["description"].apply(
                text_normalizer, args=(acronyms_dict, contractions_dict)
            )

            logging.info("Applied text_normalizer on train data")

            data_val_norm["normalized description"] = df_val["description"].apply(
                text_normalizer, args=(acronyms_dict, contractions_dict)
            )

            logging.info("Applied text_normalizer on validation data")

            data_test_norm["normalized description"] = df_test["description"].apply(
                text_normalizer, args=(acronyms_dict, contractions_dict)
            )

            logging.info("Applied text_normalizer on test data")

            data_train_norm["label"] = df_train["label"]

            data_val_norm["label"] = df_val["label"]

            data_test_norm["label"] = df_test["label"]

            X_train_norm, y_train = (
                data_train_norm["normalized description"].tolist(),
                data_train_norm["label"].tolist(),
            )

            X_val_norm, y_val = (
                data_val_norm["normalized description"].tolist(),
                data_val_norm["label"].tolist(),
            )

            X_test_norm, y_test = (
                data_test_norm["normalized description"].tolist(),
                data_test_norm["label"].tolist(),
            )

            tfidf = TfidfVectorizer(ngram_range=(1, 1))

            X_train_tfidf = tfidf.fit_transform(X_train_norm)

            X_val_tfidf = tfidf.transform(X_val_norm)

            logging.info("Transformed train,val and test data using TfidfVectorizer")

            sparse.save_npz(
                self.data_transformation_config.transformed_train_features_file_path,
                X_train_tfidf,
            )

            sparse.save_npz(
                self.data_transformation_config.transformed_val_features_file_path,
                X_val_tfidf,
            )

            save_object(
                self.data_transformation_config.transformed_test_features_file_path,
                X_test_norm,
            )

            logging.info("Saved transformed train,val and test features")

            save_object(
                self.data_transformation_config.transformed_vectorizer_file_path, tfidf
            )

            save_object(
                self.data_transformation_config.transformed_train_targets_file_path,
                y_train,
            )

            save_object(
                self.data_transformation_config.transformed_val_targets_file_path, y_val
            )

            save_object(
                self.data_transformation_config.transformed_test_targets_file_path,
                y_test,
            )

            logging.info("Saved transformed train,val and test targets")

            logging.info(
                "Exited initiate_data_transformation method of DataTransformation class"
            )

            data_transformation_artifact = DataTransformationArtifact(
                transformed_train_features_file_path=self.data_transformation_config.transformed_train_features_file_path,
                transformed_val_features_file_path=self.data_transformation_config.transformed_val_features_file_path,
                transformed_test_features_file_path=self.data_transformation_config.transformed_test_features_file_path,
                transformed_vectorizer_file_path=self.data_transformation_config.transformed_vectorizer_file_path,
                transformed_train_targets_file_path=self.data_transformation_config.transformed_train_features_file_path,
                transformed_val_targets_file_path=self.data_transformation_config.transformed_val_targets_file_path,
                transformed_test_targets_file_path=self.data_transformation_config.transformed_test_targets_file_path,
            )

            logging.info(
                f"Data Transformation artifact: {data_transformation_artifact}"
            )

            logging.info(
                "Exited initiate_data_transformation method of DataTransformation class"
            )

        except Exception as e:
            raise CustomException(e, sys)
