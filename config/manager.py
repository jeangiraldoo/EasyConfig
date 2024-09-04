import os
from app_info import config_file, user_directory, config_path

def iterate_values(line: str, action: str, arg) -> str:
    """Iterate through a setting's values (a line) and returns a value based on the provided action

    Parameters
    ----------
    line(str): Line to iterate through
    action(str): Action to take if a condition is met, in which case the return value will vary 

    Returns
    -------
    str: The return value will always be string, it's content will depend on what string was used for the action parameter
    """
    accumulator = ""
    value = ""
    line_lenght = len(line) - 1
    arg_lenght = len(arg)
    counter = 0
    for char in line:
        if(not(char == ",")):
            accumulator += char
        if(char == "," or counter == line_lenght):
            if(action == "list"):
                value += f"{accumulator}\n"
            elif(action == "search"):
                if(accumulator == arg):
                    value = "true"
                    break
            elif(action == "position"):
                if(arg == accumulator):
                    start = counter - arg_lenght
                    value = f"{start},{counter}"
                    break
            if(True):
                accumulator = ""
        counter += 1
    return value


def get_setting_values(setting_name: str, option: str):
    """Returns either the line number where a setting is located in the configuration file or the values the setting contains

    Parameters:
    setting_name(str): Name of the setting whose values we want to return
    option(str): Determines what will be returned (the values the setting has/the line number where the setting is found within the config file 
    """

    setting_lenght = len(setting_name) + 4 #4 is the amount of characters in " = ["
    file_lines: list[str] = read_main_file()
    accumulator = ""
    line_number = 0
    setting_found = False

    for i in file_lines:
        for j in i:
            accumulator += j
            if(accumulator == setting_name):
                setting_found = True 
                break
        if(not(setting_found)):
            line_number += 1

    if(setting_found):
        if(option == "position"):
            return line_number
        elif(option == "line"):
            line = file_lines[line_number]
            line_lenght = len(line)
            line_value = line[setting_lenght:(line_lenght - 1)]
            return line_value
    else:
        return "Not found"

def update_setting(setting_name: str, modification: str, option):
    """Modify an existing setting within the configuration file

    Parameters: 
    setting_name(str): Name of the setting to modify
    modification(str): Modification to be applied to the setting
    option(str): Determines what procedure will be used to apply the modification to the existing setting
    """
    file_lines = read_main_file()
    setting_position = get_setting_values(setting_name, "position")
    line = get_setting_values(setting_name, "line")

    if(line == "" or option == "r"):
        modified_setting = f"{setting_name} = [{modification}]"
    elif(option == "a"):
        modified_setting = f"{setting_name} = [{line},{modification}]" 
    file_lines[setting_position] = modified_setting

    file = open(config_path, "w")
    for i in file_lines:
        file.write(i)

def create_setting(setting_name: str):
    """Create a setting that will be stored in the configuration file

    Parameters:
    setting_name(str): This name will be added to the configuration file in the last line as 'setting_name = []'
    """
    file_lines = read_main_file()
    total_lines = len(file_lines)
    setting_to_add = f"{setting_name} = []"
    file_lines.append(setting_to_add)

    file = open(config_path, "w")
    for i in file_lines:
        file.write(i)

def read_main_file() -> list[str]:
    """Read and return the content stored in the local configuration file

    Returns:
    list of str: Each element of the list is a line in the configuration file
    """
    file = open(config_path, "r")
    file_lines = file.readlines()
    return file_lines

def create_main_file():
    """Create the configuration file that easyConfig will use"""
    if(not(os.path.exists(user_directory))):
        os.makedirs(user_directory) 
    if(not(os.path.exists(config_path))):
        open(config_path, "w")
        create_setting("Path")
