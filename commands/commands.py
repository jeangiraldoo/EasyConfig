import os
import platform
from config import config_manager
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
        line = config_manager.iterate_settings("Path", "line")
        value = config_manager.iterate_setting_values(line, "value", f"{args.app_name}")
        if(value == ""):
            parser.error("The specified app is not in the default paths and has not been added to the path list")

    os.system(f"move {args.file_name} {value}")
    print(f"{args.file_name} moved to {value}")

def remove(args, parser):
    """Remove a chosen item from the configuration file"""

    if(args.p and args.software_name == "false"):
        parser.error("The path and the software name were not specified")
    elif(args.p and args.software_name == "false"):
        parser.error("The software name was not specified")

    line = config_manager.iterate_settings("Path", "line")

    total_characters = len(line)
    value = config_manager.iterate_setting_values(line, "value", args.software_name)
    positions = config_manager.iterate_setting_values(line, "position", f"{args.software_name}->{value}")
    if(positions == ""):
        parser.error("The path specified does not exist")

    start = positions[0]
    end = positions[1]
    new_value = ""
    for i in range(total_characters):
        if(i < start or i > end):
            new_value += line[i]
    config_manager.remove_path_value(new_value)
    print(f"{args.software_name} -> {value} removed succesfully!")

def show_system_info(args):
    print(f"Operating system: {easyConfig.os_name}\nUser: {easyConfig.user}")

def list_(args):
    """List the paths that are in the "Path" setting in the configuration file"""
    if(args.d):
        print(easyConfig.get_default_paths())
    else:
        line = config_manager.iterate_settings("Path", "line")
        line_lenght = len(line)
        string_to_print = ""
        list_value = config_manager.iterate_setting_values(line, "list", "")
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
    if(not(config_manager.verify_path_exists(args.path_name))):
        parser.error("The specified path is not a valid path or does not exist in this computer")
        
    #Validates if the name or path is already in the default paths
    default_paths = easyConfig.default_paths
    for item in default_paths:
        if(default_paths[item] == args.path_name):
            parser.error(f"This path is already in use in the default paths ({item} -> {default_paths[item]})")
        elif(item == args.software_name):
            parser.error(f"This name is already in use in the default paths ({item} -> {default_paths[item]})")
    
    #Validates if the name or path is alrady in the config file
    easyConfig.config_parser.read(easyConfig.config_path)
    if(args.software_name in easyConfig.config_parser["Path"]):
        parser.error("The app name has been added in the past")
    else:
        for key in easyConfig.config_parser["Path"]:
            if(easyConfig.config_parser["Path"][key] == args.path_name):
                parser.error("The path name has been added in the past")
    config_manager.add_path_value(args.software_name, args.path_name)
