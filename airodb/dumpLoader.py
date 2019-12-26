from os import path
from dumpConverter import DumpConverter
from colorama import Fore, Style

class DumpLoader:
    @staticmethod
    def Load(filename, sessionName, debug=False):
        if path.exists(filename):
            fileHandler = open(filename, "r")
            dumpConverter = DumpConverter(sessionName)
            dumps = []
            #Ignore the first line (empty) and the second one (header)
            lineCount = 0
            for line in fileHandler:
                if lineCount > 1:
                    #Stop before the client section. Only keep AP's
                    if (line.strip()==""):
                        break
                    dumpObject = dumpConverter.convertToJSON(line)
                    if dumpObject != None:
                        dumps.append(dumpObject)
                    else:
                        if (debug):
                            print(f"{Fore.YELLOW}The line {line} has been ignored due to bad format.{Style.RESET_ALL}")
                lineCount += 1
            return dumps
        else:
            print("The file " + filename + " doesn't exist.")
            return None
            