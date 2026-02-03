import os
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

import joblib
import numpy as np
import pandas as pd
import mlflow

from sklearn.metrics import mean_squared_error

from src.datascience.constants import *
from src.datascience.utils.common import *
import urllib.request as request
from src.datascience import logger
from sklearn.metrics import r2_score
import zipfile

os.environ["MLFLOW_TRACKING_URL"] ="https://dagshub.com/damini.gupta1/datascienceproject.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="damini.gupta1"
os.environ["MLFLOW_TRACKING_PASSWORD"]="a162af0cf8c0d2ee6e9431e6e68785b7a0ff6c06"
os.environ['MLFLOW_TRACKING_INSECURE_TLS'] = 'true'
os.environ['PYTHONHTTPSVERIFY'] = '0'
@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path : Path
    metric_file_name: Path
    target_column: str
    mlflow_uri : str
    all_params : dict

class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_model_evaluation_config(self):
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN
        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(root_dir=config.root_dir,
                                                  test_data_path=config.test_data_path,
                                                  model_path=config.model_path,
                                                  metric_file_name=config.metric_file_name,
                                                  target_column=schema.name,
                                                  mlflow_uri="https://dagshub.com/damini.gupta1/datascienceproject.mlflow",
                                                  all_params=params
                                                  )

        return model_evaluation_config

class ModelEvaluation:
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config

    def eval_metrics(self,actual,pred):
        rmse= np.sqrt(mean_squared_error(actual, pred))
        mae= mean_squared_error(actual, pred)
        r2= r2_score(actual,pred)
        return rmse,mae,r2

    def log_into_mlflow(self):
        test_data= pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x= test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store= urlparse(mlflow.get_tracking_uri()).scheme
        with mlflow.start_run():
            predicted_qualities= model.predict(test_x)
            (rmse, mae, r2) = self.eval_metrics(test_y,predicted_qualities)
            scores = {"rmse":rmse, "mae":mae, "r2":r2}
            save_json(path=Path(self.config.metric_file_name),data=scores)
            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

        if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
        else:
                mlflow.sklearn.log_model(model, "model")


try:
    config= ConfigurationManager()
    model_evaluation_config= config.get_model_evaluation_config()
    model_evaluation= ModelEvaluation(config=model_evaluation_config)
    model_evaluation.log_into_mlflow()
except Exception as e:
    raise e
