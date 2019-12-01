from os import path

class DumpLoader:
    @staticmethod
    def Load(filename):
        if path.exists(filename):
            fileHandler = open(filename, "r")
            #Ignore the first line (empty) and the second one (header)
            lineCount = 0
            for line in fileHandler:
                if lineCount > 2:
                    print(line)
                lineCount += 1
            print(fileHandler.readline())
        else:
            print("Fichier " + filename + " n'existe pas")
            return None
            