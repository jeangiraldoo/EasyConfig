def showSystemInfo(args):
    if(True):#Will be changed when system flags are added
        operatingSystem = platform.system()
        user = os.getlogin()
        print(f"Operating system: {operatingSystem}")
        print(f"User: {user}")


def list_(args):
    if(args.command == "list" and args.p):

        print("List of added paths:")
        config = open("config.ec", "r")
        configContent = config.read()
        content_len = len(configContent)
        configContent = configContent[1:(content_len - 1)]
    
        string_to_print = ""

        for i in configContent:
            if(not(i == ",")):
                string_to_print += i 
            elif(i == ","):
                print(f"{string_to_print}\n")

def add(args, parser):
    if(args.p and args.software_name == "false"):
        parser.error("The name of the software was not provided")
    elif(args.p and args.path_name == "false"):
        errorMessage = "The path was not provided"
        parser.error(errorMessage)
    elif(args.p and args.path_name != "false"):
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

