from mongomock import MongoClient
from dbStorage import DBStorage
import unittest
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))

class TestDBStorageMethods(unittest.TestCase):
    def test_insert_TestWithOneEntry_Return1(self):
        mockClient = MongoClient()
        storage = DBStorage(mockClient)
        self.assertEqual(0, mockClient.airodb.airodb_dumps.count_documents({}))
        expected = [{
            "BSSID" : "64:70:02:63:0E:86",
            "FirstTimeSeen": "2019-10-30 14:31:34",
            "LastTimeSeen": "2019-10-30 14:31:56", 
            "Channel": 6, 
            "Speed": 54, 
            "Privacy": "WPA2", 
            "Cipher": "CCMP TKIP", 
            "Authentification" : "PSK", 
            "Power" : -80, 
            "NbBeacons" : 2, 
            "NbIV" : 0, 
            "LANIP" : "0.0.0.0", 
            "IDLength": 0, 
            "ESSID" : "",
            "SessionName": "MySession",
        }]
        storage.insert(expected)
        self.assertEqual(1, mockClient.airodb.airodb_dumps.count_documents({}))

    def test_insert_TestWithTwoEntries_Return2(self):
        mockClient = MongoClient()
        storage = DBStorage(mockClient)
        self.assertEqual(0, mockClient.airodb.airodb_dumps.count_documents({}))
        expected = [{
            "BSSID" : "64:70:02:63:0E:86",
            "FirstTimeSeen": "2019-10-30 14:31:34",
            "LastTimeSeen": "2019-10-30 14:31:56", 
            "Channel": 6, 
            "Speed": 54, 
            "Privacy": "WPA2", 
            "Cipher": "CCMP TKIP", 
            "Authentification" : "PSK", 
            "Power" : -80, 
            "NbBeacons" : 2, 
            "NbIV" : 0, 
            "LANIP" : "0.0.0.0", 
            "IDLength": 0, 
            "ESSID" : "",
            "SessionName": "MySession",
        }, {
            "BSSID" : "64:70:02:63:0E:87",
            "FirstTimeSeen": "2019-10-30 14:31:34",
            "LastTimeSeen": "2019-10-30 14:31:56", 
            "Channel": 6, 
            "Speed": 54, 
            "Privacy": "WPA2", 
            "Cipher": "CCMP TKIP", 
            "Authentification" : "PSK", 
            "Power" : -80, 
            "NbBeacons" : 2, 
            "NbIV" : 0, 
            "LANIP" : "0.0.0.0", 
            "IDLength": 0, 
            "ESSID" : "",
            "SessionName": "MySession1",
        }]
        storage.insert(expected)
        self.assertEqual(2, mockClient.airodb.airodb_dumps.count_documents({}))