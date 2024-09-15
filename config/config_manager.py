import os
import configparser
from app_data import easyConfig

def iterate_setting_values(line: str, action: str, arg) -> str:
    """Iterate through a setting's values (a line) and returns a value based on the provided action

    Parameters
    ----------
    line(str): Line to iterate through
    action(str): Action to take if a condition is met, in which case the return value will vary 

    Returns
    -------
    str: The return value will always be string, it's content will depend on what string was used for the action parameter
    """
    values = get_pairs(arg)
    prov_name = values[0]
    if(len(values) == 2):
        prov_path = values[1]
    line_lenght = 0
    accumulator = ""
    value = ""
    if(line != ""):
        line_lenght = len(line) - 1
    arg_lenght = len(arg)
    counter = 0

    for char in line:
        if(not(char == ",") and counter < line_lenght):
            accumulator += char
            counter += 1
            continue
        elif(counter == line_lenght):
            accumulator += char
        
        values_found = get_pairs(accumulator)
        value_name = values_found[0]
        value_path = values_found[1]

        if(action == "list"):
            value += f"{value_name} -> {value_path}\n"
        elif(action == "exists"):
            if(value_name == prov_name or value_path == prov_path):
                value = "true"
                break
        elif(action == "position" and (value_name == prov_name or value_path == prov_path)):
            start = counter - arg_lenght
            value = [start,counter]
            break
        elif(action == "value" and prov_name == value_name):
            value = value_path
            break
        accumulator = ""
        counter += 1
    return value
    

def get_pairs(value):
    separator = "->"
    value = value.replace(" ", "")
    pair = value.split(separator)
    return pair

def iterate_settings(setting_name: str, option: str):
    """Returns either the line number where a setting is located in the configuration file or the values the setting contains

    Parameters:
    setting_name(str): Name of the setting whose values we want to return
    option(str): Determines what will be returned (the values the setting has/the line number where the setting is found within the config file 
    """

    setting_lenght = len(setting_name) + 4 #4 is the amount of characters in " = ["
    file_lines: list[str] = read_config()
    accumulator = ""
    line_number = 0
    setting_found = False

    for line in file_lines:
        for char in line:
            accumulator += char
            if(accumulator == setting_name):
                setting_found = True 
                break
        if(not(setting_found)):
            line_number += 1

    if(not(setting_found)):
        return "Not found"

    if(option == "position"):
        return line_number
    elif(option == "line"):
        line = file_lines[line_number]
        line_lenght = len(line)
        line_value = line[setting_lenght:(line_lenght - 1)]
        return line_value

def remove_path_value(modification: str):
    """Modify an existing setting within the configuration file

    Parameters: 
    modification(str): Modification to be applied to the paths
    """
    
    file_lines = read_config()
    setting_position = iterate_settings("Path", "position")
    line = iterate_settings("Path", "line")

    if(modification[0] == " "):
        modification = modification.replace(" ", "", 1)

    modified_setting = f"Path = [{modification}]"
    file_lines[setting_position] = modified_setting

    file = open(easyConfig.config_path, "w")
    for i in file_lines:
        file.write(i)

def add_path_value(app_name, app_path):
    easyConfig.config_parser.read(easyConfig.config_path)
    easyConfig.config_parser["Path"][app_name] = app_path
            
    file = open(easyConfig.config_path, "w")
    easyConfig.config_parser.write(file)

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
    """Read and return the content stored in the local configuration file

    Returns:
    list of str: Each element of the list is a line in the configuration file
    """
    """
    file = open(easyConfig.config_path, "r")
    file_lines = file.readlines()
    return file_lines
    """
    easyConfig.config_parser.read(easyConfig.config_path)

def create_config():
    """Create the configuration file that easyConfig will use"""
    if(not(verify_path_exists(easyConfig.config_directory))):
        os.makedirs(easyConfig.config_directory) 
    if(not(verify_path_exists(easyConfig.config_path))):
        open(easyConfig.config_path, "w")
        add_setting("Path")

