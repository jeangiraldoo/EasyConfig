import platform 
import os 
from argparse import ArgumentParser
from commands import commands
from config import manager

manager.createMainFile()

parser = ArgumentParser(prog = "EasyConfig", description = "Automates the process of managing and installing configuration files")

subparsers = parser.add_subparsers(dest = "command")
subparser_system = subparsers.add_parser("system", help = "Returns system-specific information")
subparser_system.set_defaults(func = commands.showSystemInfo)

subparser_add = subparsers.add_parser("add", help = "Adds a path with the -p flag for future use")
subparser_add.add_argument("-p", action = "store_true", default = False)
subparser_add.add_argument("software_name", nargs = "?", default = "false")
subparser_add.add_argument("path_name", nargs = "?", default = "false")
subparser_add.set_defaults(func = lambda args: commands.add(args, subparser_add))

subparser_list = subparsers.add_parser("list", help = "Returns the configuration file paths stored")
subparser_list.add_argument("-p", action = "store_true", default = False)
subparser_list.set_defaults(func = commands.list_)

subparser_remove = subparsers.add_parser("remove", help = "Removes the selected item from the system")

args = parser.parse_args() 

if hasattr(args, "func"):
    args.func(args)

