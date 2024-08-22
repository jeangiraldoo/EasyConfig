import platform 
import os 
from argparse import ArgumentParser

def showSystemInfo(args):
    if(True):#Will be changed when system flags are added
        operatingSystem = platform.system()
        user = os.getlogin()
        print(f"Operating system: {operatingSystem}")
        print(f"User: {user}")

parser = ArgumentParser(prog = "EasyConfig",description = "Automates the process of managing and installing configuration files")

subparsers = parser.add_subparsers(dest = "command")
subparser_system = subparsers.add_parser("system", help = "Returns system-specific information")
subparser_system.set_defaults(func = showSystemInfo)

args = parser.parse_args() 

if hasattr(args, "func"):
    args.func(args)


