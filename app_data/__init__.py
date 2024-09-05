import os
import platform

class easyConfig:
    version = "0.3.2"
    config_name = "config.ec"

    def __init__(self):
        operative_system = platform.system()
        self.os_name = operative_system 
        self.user = os.getlogin()

        if(operative_system == "Windows"):
            self.config_directory = f"C:/Users/{self.user}/AppData/Local/easyConfig"
            self.default_paths = {"easyConfig":f"{self.config_directory}", "neovim":f"C:/Users/{self.user}/AppData/Local/nvim"}
        self.config_path = f"{self.config_directory}/{self.config_name}"

easyConfig = easyConfig()

