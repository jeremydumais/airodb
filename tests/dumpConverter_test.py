import unittest
import json
from os import path
import sys
sys.path.append(path.join(path.dirname(path.dirname(path.abspath(__file__))), 'airodb'))
from dumpConverter import DumpConverter


class TestDumpConverterMethods(unittest.TestCase):
    def test_convertToJSON_TestWithEmptyDump_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON(""))

    def test_convertToJSON_TestWithWhiteSpaceDump_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("   "))

    def test_convertToJSON_TestWithEmptyFieldsButValidStructure_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON(",,,,,,,,,,,,,,"))

    def test_convertToJSON_TestWithOnlyFirstFieldButValidStructure_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86,,,,,,,,,,,,,,"))

    def test_convertToJSON_TestWithOnly2FirstFieldsButValidStructure_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34,,,,,,,,,,,,,"))

    def test_convertToJSON_TestWithOnly3FirstFieldsButValidStructure_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56,,,,,,,,,,,,"))

    def test_convertToJSON_TestWithOnly4FirstFieldsButValidStructure_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6,,,,,,,,,,,"))

    def test_convertToJSON_TestWithOnly5FirstFieldsButValidStructure_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6, 54,,,,,,,,,,"))

    def test_convertToJSON_TestWithOnly6FirstFieldsButValidStructure_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6, 54, WPA2,,,,,,,,,"))

    def test_convertToJSON_TestWithOnly7FirstFieldsButValidStructure_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6, 54, WPA2, CCMP TKIP,,,,,,,,"))

    def test_convertToJSON_TestWithOnly8FirstFieldsButValidStructure_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6, 54, WPA2, CCMP TKIP, PSK,,,,,,,"))

    def test_convertToJSON_TestWithOnly9FirstFieldsButValidStructure_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6, 54, WPA2, CCMP TKIP, PSK, -80,,,,,,"))

    def test_convertToJSON_TestWithOnly10FirstFieldsButValidStructure_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6, 54, WPA2, CCMP TKIP, PSK, -80, 2,,,,,"))

    def test_convertToJSON_TestWithOnly11FirstFieldsButValidStructure_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6, 54, WPA2, CCMP TKIP, PSK, -80, 2, 0,,,,"))

    def test_convertToJSON_TestWithOnly12FirstFieldsButValidStructure_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6, 54, WPA2, CCMP TKIP, PSK, -80, 2, 0, 0.0.0.0,,,"))

    def test_convertToJSON_TestWithOnly13FirstFieldsButValidStructure_ReturnValid(self):
        converter = DumpConverter("MySession")
        expected = {
            "BSSID": "64:70:02:63:0E:86",
            "FirstTimeSeen": "2019-10-30 14:31:34",
            "LastTimeSeen": "2019-10-30 14:31:56",
            "Channel": 6,
            "Speed": 54,
            "Privacy": "WPA2",
            "Cipher": "CCMP TKIP",
            "Authentification": "PSK",
            "Power": -80,
            "NbBeacons": 2,
            "NbIV": 0,
            "LANIP": "0.0.0.0",
            "IDLength": 0,
            "ESSID": "",
            "SessionName": "MySession",
        }
        actual = converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6, 54, WPA2, CCMP TKIP, PSK, -80, 2, 0, 0.0.0.0, 0,,")
        self.assertEqual(expected, actual)

    def test_convertToJSON_TestWithComplete14FieldsValidStructure_ReturnValid(self):
        converter = DumpConverter("MySession")
        expected = {
            "BSSID": "64:70:02:63:0E:86",
            "FirstTimeSeen": "2019-10-30 14:31:34",
            "LastTimeSeen": "2019-10-30 14:31:56",
            "Channel": 6,
            "Speed": 54,
            "Privacy": "WPA2",
            "Cipher": "CCMP TKIP",
            "Authentification": "PSK",
            "Power": -80,
            "NbBeacons": 2,
            "NbIV": 0,
            "LANIP": "0.0.0.0",
            "IDLength": 6,
            "ESSID": "TESTID",
            "SessionName": "MySession",
        }
        actual = converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6, 54, WPA2, CCMP TKIP, PSK, -80, 2, 0, 0.0.0.0, 6, TESTID,")
        self.assertEqual(expected, actual)

    def test_convertToJSON_TestChannelNotInt_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6a, 54, WPA2, CCMP TKIP, PSK, -80, 2, 0, 0.0.0.0, 6, TESTID,"))

    def test_convertToJSON_TestSpeedNotInt_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6, 54W, WPA2, CCMP TKIP, PSK, -80, 2, 0, 0.0.0.0, 6, TESTID,"))

    def test_convertToJSON_TestPowerNotInt_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6, 54, WPA2, CCMP TKIP, PSK, -8l0, 2, 0, 0.0.0.0, 6, TESTID,"))

    def test_convertToJSON_TestNbBeaconsNotInt_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6, 54, WPA2, CCMP TKIP, PSK, -80, 2a, 0, 0.0.0.0, 6, TESTID,"))

    def test_convertToJSON_TestNbIVNotInt_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6, 54, WPA2, CCMP TKIP, PSK, -80, 2, 0a, 0.0.0.0, 6, TESTID,"))

    def test_convertToJSON_TestIDLengthNotInt_ReturnNone(self):
        converter = DumpConverter("MySession")
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34, 2019-10-30 14:31:56, 6, 54, WPA2, CCMP TKIP, PSK, -80, 2, 0, 0.0.0.0, 6a, TESTID,"))

    def test_convertToJSON_TestEmptyStringSessionName_ReturnNone(self):
        try:
            converter = DumpConverter("")
            raise AssertionError("Constructor should have failed")
        except ValueError:
            pass

    def test_convertToJSON_TestNoneSessionName_ReturnNone(self):
        try:
            converter = DumpConverter(None)
            raise AssertionError("Constructor should have failed")
        except ValueError:
            pass

    def test_convertToJSON_TestWhiteSpacesSessionName_ReturnNone(self):
        try:
            converter = DumpConverter("  ")
            raise AssertionError("Constructor should have failed")
        except ValueError:
            pass


if __name__ == '__main__':
    unittest.main()
