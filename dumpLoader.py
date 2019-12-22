from os import path
from dumpConverter import DumpConverter
from dbStorage import DBStorage
from colorama import Fore, Style

class DumpLoader:
    @staticmethod
    def Load(filename, sessionName):
        if path.exists(filename):
            fileHandler = open(filename, "r")
            storage = DBStorage()
            dumpConverter = DumpConverter(sessionName)
            dumps = []
            #Ignore the first line (empty) and the second one (header)
            lineCount = 0
            for line in fileHandler:
                if lineCount > 1:
                    dumpObject = dumpConverter.convertToJSON(line)
                    if dumpObject != None:
                        dumps.append(dumpObject)
                    else:
                        print(f"{Fore.YELLOW}The line {line} has been ignored due to bad format.{Style.RESET_ALL}")
                lineCount += 1
            return dumps
            #storage.insert(dumps)   
        else:
            print("The file " + filename + " doesn't exist.")
            return None
            