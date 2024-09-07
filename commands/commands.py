import os
import platform
from config import manager
from app_data import easyConfig

def handle_arguments(args):
    """Process optional flags used when running easyConfig"""
    if(args.v):
        print(f"EasyConfig {easyConfig.version}")

def install(args, parser):
    """Install configuration files in the directory where the corresponding application expects to find them"""
    try:
        app_path = easyConfig.default_paths[args.app_name]
    except KeyError:
        parser.error("The specified app has not been added to the path list")

    os.system(f"move {args.file_name} {app_path}")

def remove(args, parser):
    """Remove a chosen item from the configuration file"""
    if(args.p and args.software_name == "false" and args.path_name == "false"):
        parser.error("The path and the software name were not specified")
    elif(args.p and args.path_name == "false"):
        parser.error("The path was not specified")
    elif(args.p and args.software_name == "false"):
        parser.error("The software name was not specified")

    line = manager.iterate_settings("Path", "line")
    exists = manager.iterate_values(line, "search", f"{args.software_name}->{args.path_name}")
    if(exists != "true"):
        parser.error("The path specified does not exist")

    total_characters = len(line)
    position_start = ""
    position_end = ""
    positions = manager.iterate_values(line, "position", f"{args.software_name}->{args.path_name}")
    counter = 0
    comma_position = 0 #used to know where each position starts and end
    for i in positions:
        if(i == ","):
            comma_position = counter 
        counter += 1

    start = int(positions[:comma_position])
    end = int(positions[comma_position + 1:])
    new_value = ""
    for i in range(total_characters):
        if(i < start or i > end):
            new_value += line[i]
    manager.update_setting("Path", new_value, "r")
    print(f"{args.software_name}:{args.path_name} removed succesfully!")

def show_system_info(args):
    print(f"Operating system: {easyConfig.os_name}\nUser: {easyConfig.user}")

def list_(args):
    """List the paths that are in the "Path" setting in the configuration file"""
    if(args.d):
        print(easyConfig.get_default_paths())
    else:
        line = manager.iterate_settings("Path", "line")
        line_lenght = len(line)
        string_to_print = ""
        list_value = manager.iterate_values(line, "list", "")
        if(list_value == ""):
            print("There's no user-defined paths in the configuration file.\nUse the 'add' command with the '-p' flag to create one, or use the built-in default paths.")
        else:
            print(f"List of added paths:\n{list_value}")

def add(args, parser):
    """Add a software_name/path pair to the "Path" setting in the configuration file"""
    if(args.p and args.software_name == "false"):
        parser.error("The name of the software was not provided")
    if(args.p and args.path_name == "false"):
        parser.error("The path was not provided")
    if(not(manager.verify_path_exists(args.path_name))):
        parser.error("The specified path is not a valid path or does not exist in this computer")
        
    line = manager.iterate_settings("Path", "line")
    text_to_add = f"{args.software_name}->{args.path_name}"
    entry_exists: str = manager.iterate_values(line, "search", text_to_add)

    if(entry_exists == "true"):
        parser.error("The name or path has been added in the past")

    manager.update_setting("Path", text_to_add, "a")
    print(f"{text_to_add} added")
