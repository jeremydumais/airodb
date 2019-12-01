class MACAddress:
    @staticmethod
    def isValid(macAddress): 
        sanitizedMACAddress = macAddress.strip().upper()
        if sanitizedMACAddress == "":
            return False
        
        #Ensure that we have 6 sections
        items = sanitizedMACAddress.split(":")
        if len(items) != 6:
            return False
        
        #Ensure that every section of the MAC Address has 2 characters
        for section in items:
            if len(section) != 2:
                return False

        #Ensure that all characters is hexadecimal
        HEXADECIMAL_CHARS = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        for character in sanitizedMACAddress:
            if character not in HEXADECIMAL_CHARS:
                return False
        return True

