import os

mainFile = "config.ec"



def getSettingData(lineNumber, setting):
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

def updateSetting(setting, modification):
    content = readMainFile()
    position = getSettingPosition(setting) 
    line = getSettingData(position, setting)
    if(line == ""):
        modifiedSetting = f"{setting}{modification}]"
    else:
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
