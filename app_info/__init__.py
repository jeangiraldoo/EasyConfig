import os
import platform

def getOperatingSystem():
    os_name = platform.system()
    return os_name

def getSystemUser():
    user = os.getlogin()
    return user

__version__ = "0.1.2"
os_name = getOperatingSystem()
os_user = getSystemUser()
config_file = "config.ec"
