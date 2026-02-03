import os
import yaml
from box.exceptions import BoxValueError

from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


def read_yaml(path_to_yaml):
    try:
        with open(path_to_yaml) as yaml_file:
            content= yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created path at {path}")
@ensure_annotations
def save_json(path,data:dict):
    with open(path,'w') as f:
        json.dump(data,f,ident=4)

    logger.info(f"json file saves at :{path}")

@ensure_annotations
def load_json(path):
    with open(path) as f:
        content= json.load(path)

    logger.info(f"json file loaded sucessfully from :{path}")
    return ConfigBox(content)
@ensure_annotations
def save_bin(data,path):
    joblib.dump(value=data,filename=path)

    logger.info(f"binary file saved at :{path}")

@ensure_annotations
def load_bin(path):
    data=joblib.load(path)
    logger.info(f"binary file loaded from :{path}")
    return data





