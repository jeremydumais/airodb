class OptionParser:
    def __init__(self, options):
        #Ensute that options is a List
        if (not isinstance(options, list)):
            raise TypeError("options")
        #Ensure list elements are tuples
        for opt in options:
            if (not isinstance(opt, tuple)):
                raise TypeError("option")

        self._options = options

    def Count(self):
        return len(self._options)

    def IsOptionExist(self, optionName):
        founded = False
        for opt in self._options:
            if (opt[0] == optionName):
                founded = True
                break
        return founded

    def IsOptionExistAndValueIsNotEmpty(self, optionName):
        isValid = False
        for opt in self._options:
            if (opt[0] == optionName and opt[1] != ""):
                isValid = True
                break
        return isValid

    def GetOptionValue(self, optionName):
        value = None
        for opt in self._options:
            if (opt[0] == optionName):
                value = opt[1]
                break
        return value