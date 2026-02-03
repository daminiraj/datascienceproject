import os
from dataclasses import dataclass
from src.datascience.constants import *
from src.datascience.utils.common import *
import urllib.request as request
from src.datascience import logger
import zipfile
from sklearn.model_selection import train_test_split
import pandas as pd

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_transformation_config(self):
        config=self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config=DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path

        )
        return  data_transformation_config

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config= config


    def train_test_splitting(self):
        data=pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir,'train.csv'),index= False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info("splitting data into training and test set")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)

try:
    config=ConfigurationManager()
    data_transformation_config= config.get_data_transformation_config()
    data_transformation=DataTransformation(config=data_transformation_config)
    data_transformation.train_test_splitting()
except Exception as e:
    raise e





