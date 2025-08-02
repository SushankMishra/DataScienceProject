import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, Dict, List
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file read successfully from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError as e:
        raise ValueError(f"Empty YAML file at {path_to_yaml}: {e}")
    except Exception as e:
        logger.error(f"Error reading YAML file at {path_to_yaml}: {e}")
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """
    Creates directories if they do not exist.
    
    Args:
        path_to_directories (list[Path]): List of directory paths to create.
    """
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Directory created: {path}")
        except Exception as e:
            logger.error(f"Error creating directory {path}: {e}")
            raise e

@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    """
    Saves a dictionary as a JSON file.
    
    Args:
        path (Path): Path to save the JSON file.
        data (dict): Data to save in the JSON file.
    """
    try:
        with open(path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
            logger.info(f"JSON file saved at {path}")
    except Exception as e:
        logger.error(f"Error saving JSON file at {path}: {e}")
        raise e

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns its content as a ConfigBox object.
    
    Args:
        path (Path): Path to the JSON file.
        
    Returns:
        ConfigBox: Content of the JSON file as a ConfigBox object.
    """
    try:
        with open(path, 'r') as json_file:
            content = json.load(json_file)
            logger.info(f"JSON file loaded successfully from {path}")
            return ConfigBox(content)
    except FileNotFoundError as e:
        logger.error(f"JSON file not found at {path}: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error loading JSON file at {path}: {e}")
        raise e

@ensure_annotations
def save_model(path: Path, model: Any) -> None:
    """
    Saves a model using joblib.
    
    Args:
        path (Path): Path to save the model.
        model (Any): Model to save.
    """
    try:
        joblib.dump(model, path)
        logger.info(f"Model saved at {path}")
    except Exception as e:
        logger.error(f"Error saving model at {path}: {e}")
        raise e

@ensure_annotations
def load_model(path: Path) -> Any:
    """
    Loads a model using joblib.
    
    Args:
        path (Path): Path to the model file.
        
    Returns:
        Any: Loaded model.
    """
    try:
        model = joblib.load(path)
        logger.info(f"Model loaded successfully from {path}")
        return model
    except FileNotFoundError as e:
        logger.error(f"Model file not found at {path}: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error loading model from {path}: {e}")
        raise e