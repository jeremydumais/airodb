class DumpConverter:
    def convertToJSON(self, dumpString):
        if dumpString.strip() == "":
            return None
        
        #Split the dump on the comma symbol
        items = dumpString.split(",")
        if len(items) != 15:
            return None

        macAddress = items[0].strip()
        if macAddress == "":
            return None

        firstTimeSeen = items[1].strip()
        if firstTimeSeen == "":
            return None

        lastTimeSeen = items[2].strip()
        if lastTimeSeen == "":
            return None

        return "{}"        
    