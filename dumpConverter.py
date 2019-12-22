from macAddress import MACAddress

class DumpConverter:
    def __init__(self, sessionName):
        if sessionName == None or sessionName.strip() == "":
            raise ValueError("sessionName")
        self.sessionName = sessionName

    def convertToJSON(self, dumpString):
        if dumpString.strip() == "":
            return None
        
        #Split the dump on the comma symbol
        items = dumpString.split(",")
        if len(items) != 15:
            return None
        
        bssID = items[0].strip()
        if bssID == "" or not MACAddress.isValid(bssID):
            return None

        firstTimeSeen = items[1].strip()
        if firstTimeSeen == "":
            return None

        lastTimeSeen = items[2].strip()
        if lastTimeSeen == "":
            return None

        channel = items[3].strip()
        if channel == "" or not self.__isValidInt(channel):
            return None

        speed = items[4].strip()
        if speed == "" or not self.__isValidInt(speed):
            return None

        privacy = items[5].strip()
        if privacy == "":
            return None

        cipher = items[6].strip()

        authentication = items[7].strip()

        power = items[8].strip()
        if power == "" or not self.__isValidInt(power):
            return None

        nbBeacons = items[9].strip()
        if nbBeacons == "" or not self.__isValidInt(nbBeacons):
            return None

        nbIV = items[10].strip()
        if nbIV == "" or not self.__isValidInt(nbIV):
            return None

        lanIP = items[11].strip()
        if lanIP == "":
            return None  

        idLength = items[12].strip()
        if idLength == "" or not self.__isValidInt(idLength):
            return None  
    
        essID = items[13].strip()

        retVal = {
            "BSSID" : bssID,
            "FirstTimeSeen": firstTimeSeen,
            "LastTimeSeen": lastTimeSeen, 
            "Channel": int(channel), 
            "Speed": int(speed), 
            "Privacy": privacy, 
            "Cipher": cipher, 
            "Authentification" : authentication, 
            "Power" : int(power), 
            "NbBeacons" : int(nbBeacons), 
            "NbIV" : int(nbIV), 
            "LANIP" : lanIP, 
            "IDLength": int(idLength), 
            "ESSID" : essID,
            "SessionName": self.sessionName,
        }    

        return retVal
    
    def __isValidInt(self, numberStr):
        try:
            return int(numberStr), True
        except ValueError:
            return False