import os
from app_info import config_file

def iterate_values(line: str, action: str, arg) -> str:
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

def get_setting_values(setting_name: str, option):
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

def update_setting(setting: str, modification: str, option):
    file_lines = read_main_file()
    setting_position = get_setting_values("Path", "position")
    line = get_setting_values(setting, "line")

    if(line == "" or option == "r"):
        modified_setting = f"{setting} = [{modification}]"
    elif(option == "a"):
        modified_setting = f"{setting} = [{line},{modification}]" 
    file_lines[setting_position] = modified_setting

    file = open(config_file, "w")
    for i in file_lines:
        file.write(i)

def create_setting(setting_name: str):
    file_lines = read_main_file()
    total_lines = len(file_lines)
    setting_to_add = f"{setting_name} = []"
    content.append(setting_to_add)

    file = open(config_file, "w")
    for i in file_lines:
        file.write(i)

def read_main_file() -> list[str]:
    file = open(config_file, "r")
    file_lines = file.readlines()

    return file_lines

#Create the configuration file for easyConfig
def create_main_file():
    if(not(os.path.exists(config_file))):
        open(config_file, "w")
        create_setting("Path")
