import os
import platform
import configparser

class easyConfig:
    config_parser = configparser.ConfigParser()
    version = "0.5.3"
    config_name = "config.ini"

    def __init__(self):
        operative_system = platform.system()
        self.os_name = operative_system 
        self.user = os.getlogin()

        if(operative_system == "Windows"):
            self.config_directory = f"C:/Users/{self.user}/AppData/Local/easyConfig"
            self.default_paths = {"easyConfig":f"{self.config_directory}", "neovim":f"C:/Users/{self.user}/AppData/Local/nvim"}
        self.config_path = f"{self.config_directory}/{self.config_name}"

    def get_default_paths(self):
        paths = ""
        for i in self.default_paths:
            paths += f"{i} -> {self.default_paths[i]}\n"
        return paths
easyConfig = easyConfig()

