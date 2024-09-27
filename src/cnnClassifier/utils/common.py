import os 
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json 
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64 

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a yaml file and return a ConfigBox object

    Args:
        path_to_yaml (Path): path lile imput

    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml, 'r') as file:
            content = yaml.safe_load(file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
    except Exception as e:
        logger.error(f"Error reading yaml file: {path_to_yaml}")
        raise e
    
@ensure_annotations
def create_dicrectories(path_to_directories: list, verbose = True):
    """create list of directories
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple directories is to be created. 
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")
    
@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data
    Args:
        path (Path): path to save json file
        data (dict): data to be saved
    """
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)
    
    logger.info(f"Data saved to {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data
    
    Args:
        path (Path): path to json file
    
    Returns:
        ConfigBox: Data as class attribures instead of dictionary
    """
    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file
    
    Args:
        data (Any): data to be saved as binnary
        path (Paht): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Data saved to {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Load binary data
    
    Args:
        path (Path): path to binary file
    
    Returns:
        Any: data saved in binary format
    """
    data = joblib.load(path)
    logger.info(f"Data loaded from {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """get size of file
    
    Args:
        path (Path): path to file
    
    Returns:
        str: size of file
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())