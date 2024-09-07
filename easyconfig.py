from argparse import ArgumentParser
from commands import commands
from config import manager

manager.create_main_file()

parser = ArgumentParser(prog = "EasyConfig", description = "Automates the process of managing and installing configuration files")
parser.add_argument("-v", action = "store_true", help = "show the app version", default = False)

subparsers = parser.add_subparsers(dest = "command")

subparser_system = subparsers.add_parser("system", help = "show system-specific information")
subparser_system.set_defaults(func = commands.show_system_info)

subparser_add = subparsers.add_parser("add", help = "add a path to the configuration file")
subparser_add.add_argument("-p", required = True, action = "store_true", help = "show the User-defined paths", default = False)
subparser_add.add_argument("software_name", type = str, nargs = "?", default = "false")
subparser_add.add_argument("path_name", type = str, nargs = "?", default = "false")
subparser_add.set_defaults(func = lambda args: commands.add(args, subparser_add))

subparser_list = subparsers.add_parser("list", help = "show the user-defined paths stored")
subparser_list.add_argument("-d", action = "store_true", help = "show the default paths available", default = False)
subparser_list.set_defaults(func = commands.list_)

subparser_remove = subparsers.add_parser("remove", help = "remove the selected item from the system")
subparser_remove.add_argument("-p", action = "store_true", help = "removes a User-defined path from the configuration file", default = False)
subparser_remove.add_argument("software_name", nargs = "?", default = "false")
subparser_remove.add_argument("path_name", nargs = "?", default = "false")
subparser_remove.set_defaults(func = lambda args: commands.remove(args, subparser_remove))

subparser_install = subparsers.add_parser("install", help = "move a config file to the path where it will be recognized by its app")
subparser_install.add_argument("file_name", default = "false")
subparser_install.add_argument("app_name", default = "false")
subparser_install.set_defaults(func = lambda args:commands.install(args, subparser_install)) 

args = parser.parse_args() 

if hasattr(args, "func"):
    args.func(args)
else:
    commands.handle_arguments(args)

