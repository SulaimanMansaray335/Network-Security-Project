import yaml
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
import os, sys
import numpy as np
import dill
import pickle

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, 'r', encoding='utf-8') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e 
    

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try: 
        dir_path = os.path.dirname(file_path)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        if replace and os.path.exists(file_path):
            os.remove(file_path)

        with open(file_path, 'w', encoding='utf-8') as file:
            yaml.dump(content, file)
    except Exception as e:
        raise NetworkSecurityException(e, sys)
