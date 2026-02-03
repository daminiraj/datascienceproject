from src.datascience.utils.common import *
from src.datascience import logger
from src.datascience.entity.config_entity import DataValidationConfig
import pandas as pd
from sklearn.model_selection import train_test_split
class DataTransformation:
    def __init__(self, config: DataValidationConfig):
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