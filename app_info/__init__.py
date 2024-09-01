import os
import platform

def get_operating_system():
    os_name = platform.system()
    return os_name

def get_system_user():
    user = os.getlogin()
    return user

def get_config_directory():
    if(os_name == "Windows"):
        path = f"C:/Users/{os_user}/AppData/Local/easyConfig"
    return path

__version__ = "0.2.2"
os_name = get_operating_system()
os_user = get_system_user()
config_file = "config.ec"
user_directory = get_config_directory()
config_path = f"{user_directory}/{config_file}" 
