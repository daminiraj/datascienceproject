import os
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from sklearn.linear_model import ElasticNet

from src.datascience.constants import *
from src.datascience.utils.common import *
from src.datascience import logger

@dataclass
class DataTrainingConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path : Path
    model_name: str
    alpha :float
    l1_ratio : float
    target_column : str

class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,
                     params_filepath=PARAMS_FILE_PATH,
                     schema_filepath=SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        create_directories([self.config.artifacts_root])



    def get_data_training_config(self):
        config= self.config.data_training
        params= self.params.ElasticNet
        schema= self.schema.TARGET_COLUMN
        create_directories([config.root_dir])

        data_training_config=DataTrainingConfig(root_dir=config.root_dir,
                           train_data_path=config.train_data_path,
                           test_data_path=config.test_data_path,
                           model_name=config.model_name,
                           alpha=params.alpha,
                           l1_ratio=params.l1_ratio,
                           target_column=schema.name
                         )

        return data_training_config

class DataTraining:
    def __init__(self,config: DataTrainingConfig):
        self.config= config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x= train_data.drop([self.config.target_column],axis=1)
        train_y = train_data[[self.config.target_column]]

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        lr= ElasticNet(alpha= self.config.alpha,l1_ratio= self.config.l1_ratio,random_state=42)
        lr.fit(train_x,train_y)
        joblib.dump(lr,os.path.join(self.config.root_dir, self.config.model_name))

try:
    config=ConfigurationManager()
    data_training_config= config.get_data_training_config()
    data_training=DataTraining(config=data_training_config)
    data_training.train()
except Exception as e:
    raise e








