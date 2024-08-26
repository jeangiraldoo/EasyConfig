from config import manager
import os
import platform

def showSystemInfo(args):
    if(True):#Will be changed when system flags are added
        operatingSystem = platform.system()
        user = os.getlogin()
        print(f"Operating system: {operatingSystem}")
        print(f"User: {user}")


def list_(args):
        print("List of added paths:")
        position = manager.getSettingPosition("Path = [")
        line = manager.getSettingData(position, "Path = [")
        lineLenght = len(line)
        string_to_print = ""
        counter = 0
        for i in line:
            counter += 1
            if(not(i == ",")):
                string_to_print += i
            if(i == ","):
                print(string_to_print)
                string_to_print = "" 
        print(string_to_print)

def add(args, parser):
    if(args.p and args.software_name == "false"):
        parser.error("The name of the software was not provided")
    elif(args.p and args.path_name == "false"):
        errorMessage = "The path was not provided"
        parser.error(errorMessage)
    elif(args.p and args.path_name != "false"):
        entryExists = checkRecord(args.software_name, args.path_name)

        if(entryExists):
            parser.error("The name or path has been added in the past")
        else:
            textToAdd = f"{args.software_name}:{args.path_name}"
            manager.updateSetting("Path = [", textToAdd)
            print(f"{args.software_name}:{args.path_name} added")

def checkRecord(name, path):
    content = manager.readMainFile()
    position = manager.getSettingPosition("Path = [")
    line = manager.getSettingData(position, "Path = [")
    stuff = ""
    for k in line:
        if(not(k == ":" or k == ",")):
            stuff += k
        else:
            if(stuff == name or stuff == path):
                return True
            else:
                stuff = ""
    
    return False
