from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_training import DataTraining


class DataTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_training(self):
        config = ConfigurationManager()
        data_training_config = config.get_data_training_config()
        data_training = DataTraining(config=data_training_config)
        data_training.train()
