import unittest
from os import path
import sys
sys.path.append(path.join(path.dirname(__file__), '..'))
from dumpConverter import DumpConverter

class TestDumpConverterMethods(unittest.TestCase):
    def test_convertToJSON_TestWithEmptyDump_ReturnNone(self):
        #self.assertTrue(1)
        converter = DumpConverter()
        self.assertEqual(None, converter.convertToJSON(""))

    def test_convertToJSON_TestWithWhiteSpaceDump_ReturnNone(self):
        converter = DumpConverter()
        self.assertEqual(None, converter.convertToJSON("   "))
    
    def test_convertToJSON_TestWithEmptyFieldsButValidStructure_ReturnNone(self):
        converter = DumpConverter()
        self.assertEqual(None, converter.convertToJSON(",,,,,,,,,,,,,,"))
    
    def test_convertToJSON_TestWithOnlyFirstFieldButValidStructure_ReturnNone(self):
        converter = DumpConverter()
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86,,,,,,,,,,,,,,"))

    def test_convertToJSON_TestWithOnly2FirstFieldsButValidStructure_ReturnNone(self):
        converter = DumpConverter()
        self.assertEqual(None, converter.convertToJSON("64:70:02:63:0E:86, 2019-10-30 14:31:34,,,,,,,,,,,,,"))

if __name__ == '__main__':
    unittest.main()