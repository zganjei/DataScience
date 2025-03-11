import os
import yaml
from src.datascience import logger
import json
# for creating and saving model in hard disk
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """ reads yaml file and returns
    Args:
        path_to_yaml
    Raises:
        ValueError
    Returns:
        ConfigBox"""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            # in Configbox you can directly use the keys, as opposed to python dictionaries
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):
    """create list of directories"""

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"created directory at {path}")

@ensure_annotations
def save_json(path: Path, data:dict):
    """save json data"""
    with open(path,"w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file save at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load data from json file"""
    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox

@ensure_annotations
def save_bin(data: Any, path:Path):
    """save binary file of some model"""
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(data: Any, path:Path):
    """load a model from binary"""
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data