import unittest
from os import path
import sys
sys.path.append(path.join(path.dirname(path.dirname(path.abspath(__file__))), 'airodb'))
from mongomock import MongoClient
from dbStorage import DBStorage


class TestDBStorageMethods_OneEntryFixture(unittest.TestCase):
    def setUp(self):
        self.mockClient = MongoClient()
        entries = [{
            "BSSID": "64:70:02:63:0E:86",
            "FirstTimeSeen": "2019-10-30 14:31:34",
            "LastTimeSeen": "2019-10-30 14:31:56",
            "SessionName": "MySession",
        }]
        self.mockClient.airodb.airodb_dumps.insert_many(entries)

    def tearDown(self):
        self.mockClient.close()

    def test_insert_TestOneDocumentAdded_Return1(self):
        newDocument = [{
            "BSSID": "64:70:02:63:1E:86",
            "FirstTimeSeen": "2019-10-30 14:32:34",
            "LastTimeSeen": "2019-10-30 14:32:56",
            "SessionName": "MySession",
        }]
        dbStorage = DBStorage(self.mockClient)
        dbStorage.insert(newDocument)
        self.assertEqual(2, self.mockClient.airodb.airodb_dumps.count_documents({}))

    def test_isSessionNameAlreadyExist_TestWithNonExistantSession_ReturnFalse(self):
        dbStorage = DBStorage(self.mockClient)
        self.assertFalse(dbStorage.isSessionNameAlreadyExist("test")) 

    def test_isSessionNameAlreadyExist_TestWithExistantSession_ReturnTrue(self):
        dbStorage = DBStorage(self.mockClient)
        self.assertTrue(dbStorage.isSessionNameAlreadyExist("MySession")) 

class TestDBStorageMethods_TwoEntriesFixture(unittest.TestCase):
    def setUp(self):
        self.mockClient = MongoClient()
        entries = [{
            "BSSID" : "64:70:02:63:0E:86",
            "FirstTimeSeen": "2019-10-30 14:31:34",
            "LastTimeSeen": "2019-10-30 14:31:56", 
            "SessionName": "MySession",
        }, {
            "BSSID" : "64:70:02:63:0E:87",
            "FirstTimeSeen": "2019-10-30 14:31:34",
            "LastTimeSeen": "2019-10-30 14:31:56", 
            "SessionName": "MySession1",
        }]
        self.mockClient.airodb.airodb_dumps.insert_many(entries)

    def tearDown(self):
        self.mockClient.close()

    def test_insert_TestTwoDocumentAdded_Return2(self):
        newDocuments = [{
            "BSSID": "64:70:02:63:1E:86",
            "FirstTimeSeen": "2019-10-30 14:32:34",
            "LastTimeSeen": "2019-10-30 14:32:56",
            "SessionName": "MySession",
        }, {
            "BSSID": "64:70:02:63:2E:86",
            "FirstTimeSeen": "2019-10-30 14:34:34",
            "LastTimeSeen": "2019-10-30 14:34:56",
            "SessionName": "MySession",
        }]
        dbStorage = DBStorage(self.mockClient)
        dbStorage.insert(newDocuments)
        self.assertEqual(4, self.mockClient.airodb.airodb_dumps.count_documents({}))

    def test_insert_TestOneDocumentAndCheckSessionName_ReturnValid(self):
        newDocument = [{
            "BSSID": "64:70:02:63:1E:86",
            "FirstTimeSeen": "2019-10-30 14:32:34",
            "LastTimeSeen": "2019-10-30 14:32:56",
            "SessionName": "MySessionTest",
        }]
        dbStorage = DBStorage(self.mockClient)
        dbStorage.insert(newDocument)
        self.assertEqual(3, self.mockClient.airodb.airodb_dumps.count_documents({}))
        self.assertTrue(dbStorage.isSessionNameAlreadyExist("MySessionTest"))

    def test_isEntryExist_TestWithExisting_ReturnTrue(self):
        dbStorage = DBStorage(self.mockClient)
        expected = {
            "BSSID": "64:70:02:63:0E:87",
            "FirstTimeSeen": "2019-10-30 14:31:34",
            "LastTimeSeen": "2019-10-30 14:31:56",
            "SessionName": "MySession1",
        }
        self.assertTrue(dbStorage.isEntryExist(expected))
    
    def test_isEntryExist_TestWithDifferentBSSID_ReturnFalse(self):
        dbStorage = DBStorage(self.mockClient)
        expected = {
            "BSSID": "64:70:02:63:0E:88",
            "FirstTimeSeen": "2019-10-30 14:31:34",
            "LastTimeSeen": "2019-10-30 14:31:56",
            "SessionName": "MySession1",
        }
        self.assertFalse(dbStorage.isEntryExist(expected))

    def test_isEntryExist_TestWithDifferentFTS_ReturnFalse(self):
        dbStorage = DBStorage(self.mockClient)
        expected = {
            "BSSID": "64:70:02:63:0E:87",
            "FirstTimeSeen": "2019-10-30 14:31:36",
            "LastTimeSeen": "2019-10-30 14:31:56",
            "SessionName": "MySession1",
        }
        self.assertFalse(dbStorage.isEntryExist(expected))

    def test_isEntryExist_TestWithDifferentLTS_ReturnFalse(self):
        dbStorage = DBStorage(self.mockClient)
        expected = {
            "BSSID": "64:70:02:63:0E:87",
            "FirstTimeSeen": "2019-10-30 14:31:34",
            "LastTimeSeen": "2019-10-30 14:31:57",
            "SessionName": "MySession1",
        }
        self.assertFalse(dbStorage.isEntryExist(expected))

    def test_isEntryExist_TestWithDifferentSessionName_ReturnFalse(self):
        dbStorage = DBStorage(self.mockClient)
        expected = {
            "BSSID": "64:70:02:63:0E:87",
            "FirstTimeSeen": "2019-10-30 14:31:34",
            "LastTimeSeen": "2019-10-30 14:31:56",
            "SessionName": "MySession2",
        }
        self.assertFalse(dbStorage.isEntryExist(expected))

class TestDBStorageMethods(unittest.TestCase):
    def test_isSessionNameAlreadyExist_TestWithEmptyStringSessionNoEntries_ThrowValueError(self):
        mockClient = MongoClient()
        storage = DBStorage(mockClient)
        try:
            storage.isSessionNameAlreadyExist("")
            raise AssertionError("Method should have failed")
        except ValueError:
            pass

    def test_isSessionNameAlreadyExist_TestWithWhiteSpacesStringSessionNoEntries_ThrowValueError(self):
        mockClient = MongoClient()
        storage = DBStorage(mockClient)
        try:
            storage.isSessionNameAlreadyExist("   ")
            raise AssertionError("Method should have failed")
        except ValueError:
            pass

    def test_isSessionNameAlreadyExist_TestWithNoneSessionNoEntries_ThrowTypeError(self):
        mockClient = MongoClient()
        storage = DBStorage(mockClient)
        try:
            storage.isSessionNameAlreadyExist(None)
            raise AssertionError("Method should have failed")
        except TypeError:
            pass

    def test_isSessionNameAlreadyExist_TestWithIntSessionNoEntries_ThrowTypeError(self):
        mockClient = MongoClient()
        storage = DBStorage(mockClient)
        try:
            storage.isSessionNameAlreadyExist(12)
            raise AssertionError("Method should have failed")
        except TypeError:
            pass

    def test_isSessionNameAlreadyExist_TestWithEmptyListSessionNoEntries_ThrowTypeError(self):
        mockClient = MongoClient()
        storage = DBStorage(mockClient)
        try:
            storage.isSessionNameAlreadyExist([])
            raise AssertionError("Method should have failed")
        except TypeError:
            pass
