import platform 
import os 
from argparse import ArgumentParser

def showSystemInfo(args):
    if(True):#Will be changed when system flags are added
        operatingSystem = platform.system()
        user = os.getlogin()
        print(f"Operating system: {operatingSystem}")
        print(f"User: {user}")

def create(args, parser):
    if(args.software_name == "false"):
        parser.error("The name of the software was not provided")
    elif(args.p and args.path_name == "false"):
        errorMessage = "The path was not provided"
        parser.error(errorMessage)
    else:
        paths[args.software_name] = args.path_name

paths = {}

parser = ArgumentParser(prog = "EasyConfig", description = "Automates the process of managing and installing configuration files")

subparsers = parser.add_subparsers(dest = "command")
subparser_system = subparsers.add_parser("system", help = "Returns system-specific information")
subparser_system.set_defaults(func = showSystemInfo)

subparser_create = subparsers.add_parser("create", help = "Creates a configuration file or adds a path with the -p flag for future use")
subparser_create.add_argument("-p", action = "store_true", default = False)
subparser_create.add_argument("software_name", nargs = "?", default = "false")
subparser_create.add_argument("path_name", nargs = "?", default = "false")
subparser_create.set_defaults(func = lambda args: create(args, subparser_create))

args = parser.parse_args() 

if hasattr(args, "func"):
    args.func(args)


