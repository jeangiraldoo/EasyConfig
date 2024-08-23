import platform 
import os 
from argparse import ArgumentParser

def createECFile():
    if(not(os.path.exists("config.ec"))):
        config = open("config.ec", "w")
        config.write("[]")

def showSystemInfo(args):
    if(True):#Will be changed when system flags are added
        operatingSystem = platform.system()
        user = os.getlogin()
        print(f"Operating system: {operatingSystem}")
        print(f"User: {user}")

def checkRecord(name, path):
    config = open("config.ec", "r")
    configContent = config.read()
    char_num = len(configContent)
    configContent = configContent[1:(char_num - 1)]
    
    stuff = ""
    for i in configContent:
        if(not(i == ":" or i == ",")):
            stuff += i
        else:
            if(stuff == name or stuff == path):
                return True
            else:
                stuff = ""
    return False

def create(args, parser):
    if(args.software_name == "false"):
        parser.error("The name of the software was not provided")
    elif(args.p and args.path_name == "false"):
        errorMessage = "The path was not provided"
        parser.error(errorMessage)
    else:
        config = open("config.ec", "r")
        configContent = config.read()
        char_num = len(configContent)
        configContent = configContent[1:(char_num - 1)]
        entryExists = checkRecord(args.software_name, args.path_name)

        if(entryExists):
            parser.error("The name or path has been added in the past")
        else:
            configContent = f"{args.software_name}:{args.path_name},{configContent}"
            config = open("config.ec","w")
            config.write(f"[{configContent}]")
            print(f"{args.software_name}:{args.path_name} added")

createECFile()

parser = ArgumentParser(prog = "EasyConfig", description = "Automates the process of managing and installing configuration files")

subparsers = parser.add_subparsers(dest = "command")
subparser_system = subparsers.add_parser("system", help = "Returns system-specific information")
subparser_system.set_defaults(func = showSystemInfo)

subparser_create = subparsers.add_parser("create", help = "Creates a configuration file or adds a path with the -p flag for future use")
subparser_create.add_argument("-p", action = "store_true", default = False)
subparser_create.add_argument("software_name", nargs = "?", default = "false")
subparser_create.add_argument("path_name", nargs = "?", default = "false")
subparser_create.set_defaults(func = lambda args: create(args, subparser_create))

#subparser_path = subparsers.add_parser("list", help = "Returns the configuration file paths stored")
#subparser_path.set_defaults(func = list_)

args = parser.parse_args() 

if hasattr(args, "func"):
    args.func(args)

