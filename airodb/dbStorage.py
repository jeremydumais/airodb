import pymongo
import sys
from pymongo import MongoClient
from colorama import Fore, Style


class DBStorage():
    def __init__(self, mongoClient=None):
        if (mongoClient is None):
            try:
                print("Connecting to the local MongoDB instance...  ", end=" ", flush=True)
                self._client = MongoClient()
                self._db = self._client["airodb"]
                self.dumps = self._db.airodb_dumps
                # Fix: start a count command to force the client to connect
                self.dumps.count_documents({})
                print(f"{Fore.GREEN}Done{Style.RESET_ALL}")
            except pymongo.errors.ServerSelectionTimeoutError:
                print(f"{Fore.RED}Error{Style.RESET_ALL}")
                print("Unable to connect to the local MongoDB instance")
                sys.exit(2)
        else:
            self._client = mongoClient
            self._db = self._client.airodb
            self.dumps = self._db.airodb_dumps

    def __del__(self):
        self._client.close()

    def insert(self, dumps):
        self.dumps.insert_many(dumps)

    def isSessionNameAlreadyExist(self, sessionName):
        if (not isinstance(sessionName, str)):
            raise TypeError("sessionName")
        if (sessionName.strip() == ""):
            raise ValueError("sessionName")
        return (self.dumps.count_documents({"SessionName": sessionName}) > 0)

    def isEntryExist(self, entry):
        return (self.dumps.count_documents({"SessionName": entry["SessionName"],
                "BSSID": entry["BSSID"],
                "FirstTimeSeen": entry["FirstTimeSeen"],
                "LastTimeSeen": entry["LastTimeSeen"]}) > 0)
