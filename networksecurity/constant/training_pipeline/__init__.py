import os 
import sys
import numpy as np 
import pandas as pd

"""
defining common constant variable for training pipeline
"""
TARGET_COLUMN='Result'
PIPELINE_NAME:str='NetworkSecurity'
ARTIFACT_DIR: str='Artifacts'
FILE_NAME: str ="phisingData.csv"


TRAIN_FILE_NAME:str='train.csv'
TEST_FILE_NAME:str='test.csv'

SCHEMA_FILE_PATH=os.path.join("data_schema","schema.yaml")

"""
Data Ingestion related constant start with Data_Ingestion var name
"""

DATA_INGESTION_COLLECTION_NAME: str ='NetworkData'
DATA_INGESTION_DATABASE_NAME: str = "BuzzAI"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float =0.2

"""
data validation related constant start with data_validation var name
"""
DATA_VALIDATION_DIR_NAME:str="data_validation"
DATA_VALIDATION_VALID_DIR:str="validated"
DATA_VALIDATION_INVALID_DIR:str="invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR:str="drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str="report.ymal"

"""
Data transformation related constant start with DATA_TRANSFORMATION Var Name
"""
DATA_TRANSFORMATION_DIR_NAME:str="data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str="transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str="transformed_object"
PREPROCESSING_OBJECT_FILE_NAME:str="preprocessing.pkl"

# knn imputer to replace nan values
DATA_TRANSFORMATION_TRANSFORMED_IMPUTER_PARAMS:dict={
    "missing_values":np.nan,
    "n_neighbors":3,
    "weights":"uniform",
}