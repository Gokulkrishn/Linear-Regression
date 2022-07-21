import pandas as pd
import numpy as np
import yaml
import os,sys
import dill
from housing.exception import HousingException
from housing.constants import *


def read_yaml_file(file_path:str) -> dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e

def load_data(file_path:str, schema_file_path:str) -> pd.DataFrame:
    try:
        dataset_schema = read_yaml_file(schema_file_path)
        schema = dataset_schema[DATASET_SCHEMA_COLUMN_KEY]

        df = pd.read_csv(file_path)

        error_message = ''
        
        for column in df.columns:
            if column in schema.keys():
                df[column].astype(schema[column])
            else:
                error_message += f"{column} not present in schema columns"
        if len(error_message) > 0:
            raise Exception(error_message)
        return df        

    except Exception as e:
        raise HousingException(e,sys) from e

def save_numpy_array_data(file_path:str,array:np.array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as f:
            np.save(f,array)
    except Exception as e:
        raise HousingException(e,sys) from e    

def save_object(file_path:str,obj:str):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as f:
            dill.dump(obj,f)
    except Exception as e:
        raise HousingException(e,sys) from e