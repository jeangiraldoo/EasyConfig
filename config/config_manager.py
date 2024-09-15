import os
import configparser
from app_data import easyConfig

def remove_path_value(app_name: str):
    """Remove an existing key/value pair in the Path section of the configuration file

    Parameters: 
    app_name(str): Name of the app, represented as a key
    """
    file = open(easyConfig.config_path, "w")
    easyConfig.config_parser.remove_option("Path", app_name)
    easyConfig.config_parser.write(file)
    print(f"{app_name} removed successfully!")

def add_path_value(app_name, app_path):
    easyConfig.config_parser.read(easyConfig.config_path)
    easyConfig.config_parser["Path"][app_name] = app_path
            
    file = open(easyConfig.config_path, "w")
    easyConfig.config_parser.write(file)
    print(f"{app_name} added successfully!")

def add_setting(setting_name: str):
    """Create a setting that will be stored in the configuration file

    Parameters:
    setting_name(str): This name will be added to the configuration file in the last line as 'setting_name = []'
    """
    easyConfig.config_parser[setting_name] = {}
    file = open(easyConfig.config_path, "w")
    easyConfig.config_parser.write(file)

def verify_path_exists(path) -> bool:
    if(os.path.exists(path)):
        return True 
    return False

def read_config() -> list[str]:
    easyConfig.config_parser.read(easyConfig.config_path)

def create_config():
    """Create the configuration file that easyConfig will use"""
    if(not(verify_path_exists(easyConfig.config_directory))):
        os.makedirs(easyConfig.config_directory) 
    if(not(verify_path_exists(easyConfig.config_path))):
        open(easyConfig.config_path, "w")
        add_setting("Path")

