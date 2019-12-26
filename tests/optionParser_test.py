import unittest
from os import path
import sys
sys.path.append(path.join(path.dirname(path.dirname(path.abspath(__file__))), 'airodb'))
from optionParser import OptionParser

class TestOptionParserMethods(unittest.TestCase):
    def test_constructor_TestWithNoneOptions_ThrowTypeError(self):
        try:
            parser = OptionParser(None)
            raise AssertionError("Constructor should have failed")
        except TypeError:
            pass   

    def test_constructor_TestWithStringOptions_ThrowTypeError(self):
        try:
            parser = OptionParser("test")
            raise AssertionError("Constructor should have failed")
        except TypeError:
            pass   

    def test_constructor_TestWithEmptyListOptions_ReturnValid(self):
        parser = OptionParser([])
        self.assertEqual(0, parser.Count())

    def test_constructor_TestWithOneShortOptListOptions_ReturnValid(self):
        parser = OptionParser([("-s", "test")])
        self.assertEqual(1, parser.Count())
    
    def test_constructor_TestWithTwoShortOptListOptions_ReturnValid(self):
        parser = OptionParser([("-s", "test"), ("-i", "eth0")])
        self.assertEqual(2, parser.Count())
    
    def test_constructor_TestWithOneNotTupleStringOptElement_ThrowTypeError(self):
        try:
            parser = OptionParser(["test"])
            raise AssertionError("Constructor should have failed")
        except TypeError:
            pass 

    def test_constructor_TestWithOneNotTupleIntOptElement_ThrowTypeError(self):
        try:
            parser = OptionParser([3])
            raise AssertionError("Constructor should have failed")
        except TypeError:
            pass   
  
    def test_Count_TestWithOneShortOptListOptions_Return1(self):
        parser = OptionParser([("-s", "test")])
        self.assertEqual(1, parser.Count())
    
    def test_Count_TestWithTwoShortOptListOptions_Return2(self):
        parser = OptionParser([("-s", "test"), ("-i", "eth0")])
        self.assertEqual(2, parser.Count())

    def test_IsOptionExist_TestWithDashS_ReturnTrue(self):
        parser = OptionParser([("-s", "test")])
        self.assertTrue(parser.IsOptionExist("-s"))
    
    def test_IsOptionExist_TestWithDashW_ReturnFalse(self):
        parser = OptionParser([("-s", "test")])
        self.assertFalse(parser.IsOptionExist("-w"))
    
    def test_IsOptionExist_TestWithSessionLongFormat_ReturnTrue(self):
        parser = OptionParser([("--session", "test")])
        self.assertTrue(parser.IsOptionExist("--session"))

    def test_IsOptionExist_TestWithInterfaceLongFormat_ReturnFalse(self):
        parser = OptionParser([("--session", "test")])
        self.assertFalse(parser.IsOptionExist("--interface"))

    def test_GetOptionValue_TestWithSessionLongFormat_ReturnTrue(self):
        parser = OptionParser([("--session", "test")])
        self.assertEqual("test", parser.GetOptionValue("--session"))

    def test_GetOptionValue_TestWithSessionLongFormatTwoOpts_ReturnTrue(self):
        parser = OptionParser([("--session", "test"), ("--interface", "eth0")])
        self.assertEqual("test", parser.GetOptionValue("--session"))
    
    def test_GetOptionValue_TestWithInterfaceLongFormatTwoOpts_ReturnTrue(self):
        parser = OptionParser([("--session", "test"), ("--interface", "eth0")])
        self.assertEqual("eth0", parser.GetOptionValue("--interface"))
   
    def test_GetOptionValue_NotExistingOpt_ReturnNone(self):
        parser = OptionParser([("--session", "test"), ("--interface", "eth0")])
        self.assertEqual(None, parser.GetOptionValue("--bla"))

    def test_IsOptionExistAndValueIsNotEmpty_TestWithDashSAndValue_ReturnTrue(self):
        parser = OptionParser([("-s", "test")])
        self.assertTrue(parser.IsOptionExistAndValueIsNotEmpty("-s"))

    def test_IsOptionExistAndValueIsNotEmpty_TestWithDashSAndEmptyValue_ReturnFalse(self):
        parser = OptionParser([("-s", "")])
        self.assertFalse(parser.IsOptionExistAndValueIsNotEmpty("-s"))

    def test_IsOptionExistAndValueIsNotEmpty_TestWithSessionAndValueLongFormat_ReturnTrue(self):
        parser = OptionParser([("--session", "test")])
        self.assertTrue(parser.IsOptionExistAndValueIsNotEmpty("--session"))

    def test_IsOptionExistAndValueIsNotEmpty_TestWithSessionAndEmptyValueLongFormat_ReturnFalse(self):
        parser = OptionParser([("--session", "")])
        self.assertFalse(parser.IsOptionExistAndValueIsNotEmpty("--session"))

    def test_IsOptionExistAndValueIsNotEmpty_TestWithInterfaceAndValueLongFormat_ReturnTrue(self):
        parser = OptionParser([("--session", "test"), ("--interface", "eth0")])
        self.assertTrue(parser.IsOptionExistAndValueIsNotEmpty("--interface"))

    def test_IsOptionExistAndValueIsNotEmpty_TestWithInterfaceAndEmptyValueLongFormat_ReturnFalse(self):
        parser = OptionParser([("--session", ""), ("--interface", "")])
        self.assertFalse(parser.IsOptionExistAndValueIsNotEmpty("--interface"))

    def test_GetOptionValueOverload_TestWithSessionLongFormatTwoOpts_ReturnTrue(self):
        parser = OptionParser([("--session", "test"), ("--interface", "eth0")])
        self.assertEqual("test", parser.GetOptionValue("-s", "--session"))

    def test_GetOptionValueOverload_TestWithSessionShortFormatTwoOpts_ReturnTrue(self):
        parser = OptionParser([("-s", "test"), ("--interface", "eth0")])
        self.assertEqual("test", parser.GetOptionValue("-s", "--session"))

    def test_GetOptionValueOverload_TestWithSeShortFormatTwoOpts_ReturnFalse(self):
        parser = OptionParser([("-s", "test"), ("--interface", "eth0")])
        self.assertEqual(None, parser.GetOptionValue("-se", "--session"))
    