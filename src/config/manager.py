import os

mainFile = "config.ec"


def search_in_path(value):
    path_position = getSettingPosition("Path = [")
    print(path_position)
    data = getSettingData(path_position, "Path = [")
    lenght = len(data) - 1
    print(f"Len: {lenght}")

    value_in_path = ""
    counter = 0
    for i in data:
        if(not(i == ",")):
            value_in_path += i
        if(i == "," or counter == lenght):
            if(value_in_path == value):
                print(f"Value: {value_in_path}")
                print(f"Len: {lenght}")
                print(f"Counter: {counter}")
                return True
            else:
                value_in_path = ""

        counter += 1
        print(value_in_path)

    print(value_in_path) 
    print(counter)
    return False


def get_position_in_path(value):
    path_position = getSettingPosition("Path = [")
    data = getSettingData(path_position, "Path = [")
    lenght = len(data) - 1
    value_lenght = len(value)
    print("lenght siuu: " + str(lenght))

    value_in_path = ""
    start = 0
    counter = 0
    for i in data:
        if(i != ","):
            value_in_path += i
        if(i == "," or counter == lenght):
            if(value_in_path == value):
                start = counter - value_lenght
                print(f"counter: {counter}")
                print(f"Lenght: {value_lenght}")
                print(f"Start: {start}")
                return [start, counter]
            else:
                value_in_path = ""
        counter += 1



def getSettingData(lineNumber, setting):
    print(lineNumber)
    content = readMainFile()
    settingLenght = len(setting)
    line = content[lineNumber]
    contentLenght = len(line)
    value = line[settingLenght:contentLenght - 1]
    return value

def getSettingPosition(setting):
    content = readMainFile()

    accumulator = ""
    position = 0
    for i in content:
        position += 1
        for j in i:
            accumulator += j
            if(accumulator == setting):
                print(position - 1)
                return position - 1 

def searchSetting(setting):
    content = readMainFile()

    if(len(content) == 0):
        return False

    accumulator = ""
    for position in content:
        for string in content[position]:
            accumulator += j
            if(accumulator == setting):
                return True

def updateSetting(setting, modification, option):
    content = readMainFile()
    position = getSettingPosition(setting) 
    line = getSettingData(position, setting)
    if(line == "" or option == "r"):
        modifiedSetting = f"{setting}{modification}]"
    elif(option == "a"):
        modifiedSetting = f"{setting}{line},{modification}]" 
    content[position] = modifiedSetting
    file = open(mainFile, "w")
    for i in content:
        file.write(i)

def createSetting(setting):
    content = readMainFile()
    totalLines = len(content)
    content.append(setting)

    file = open(mainFile, "w")
    for i in content:
        file.write(i)

def readMainFile():
    file = open(mainFile, "r")
    content = file.readlines()

    return content

#Create the configuration file for easyConfig
def createMainFile():
    if(not(os.path.exists(mainFile))):
        open(mainFile, "w")
        createSetting("Path = []")
