import unittest
from os import path
import sys
sys.path.append(path.join(path.dirname(path.dirname(path.abspath(__file__))), 'airodb'))
from macAddress import MACAddress


class TestMACAddressMethods(unittest.TestCase):
    def test_isValid_TestWithEmptyMAC_ReturnFalse(self):
        self.assertFalse(MACAddress.isValid(""))

    def test_isValid_TestWithWhiteSpaceMAC_ReturnFalse(self):
        self.assertFalse(MACAddress.isValid("  "))

    def test_isValid_TestWithOnly5SectionsMAC_ReturnFalse(self):
        self.assertFalse(MACAddress.isValid("64:70:02:63:0E"))

    def test_isValid_TestWith7SectionsMAC_ReturnFalse(self):
        self.assertFalse(MACAddress.isValid("64:70:02:63:0E:86:EE"))

    def test_isValid_TestWith6SectionsButEmptyMAC_ReturnFalse(self):
        self.assertFalse(MACAddress.isValid(":::::"))

    def test_isValid_TestWithInvalidCharGMAC_ReturnFalse(self):
        self.assertFalse(MACAddress.isValid("G4:70:02:63:0E:86"))

    def test_isValid_TestWithInvalidCharCommaMAC_ReturnFalse(self):
        self.assertFalse(MACAddress.isValid("64:7,:02:63:0E:86"))

    def test_isValid_TestWithOneCharMissingMAC_ReturnFalse(self):
        self.assertFalse(MACAddress.isValid("64:7:02:63:0E:86"))


if __name__ == '__main__':
    unittest.main()
