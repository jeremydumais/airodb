from dumpLoader import DumpLoader
from optionParser import OptionParser
import getopt
import sys
from colorama import Fore, Style

def main():
     try:
          #print(sys.argv)
          opts, args = getopt.getopt(sys.argv[1:],"hs:vi:v",["help","session=", "interface="])
     except getopt.GetoptError as err:
          print(f"{Fore.RED}{str(err)}{Style.RESET_ALL}")
          usage()
          sys.exit(2)
     optionParser = OptionParser(opts)
     validateRequiredArgs(optionParser)
     #print(optionParser.GetOptionValue("-s") or optionParser.GetOptionValue("-session"))
     #sys.exit(2)
     #Check if that session name already exist

     #Launch the airodump process
     #Enter the main loop to process the dumps
     dumps = DumpLoader.Load("dump/dump.csv", )

def validateRequiredArgs(optionParser):
     
     sessionFound = False
     interfaceFound = False
     if (optionParser.IsOptionExistAndValueIsNotEmpty("-s") or optionParser.IsOptionExistAndValueIsNotEmpty("--session")):
          sessionFound = True
     if (optionParser.IsOptionExistAndValueIsNotEmpty("-i") or optionParser.IsOptionExistAndValueIsNotEmpty("--interface")):
          interfaceFound = True
     if (optionParser.IsOptionExist("-h") or optionParser.IsOptionExist("--help")):
          usage()
          sys.exit(0)
     if not sessionFound or not interfaceFound:
          usage()
          sys.exit(2)

#ParseOptionClass

def usage():
     print("Usage: airodb --session <sessionName> --interface <interfaceName>")
     print("  -s | --session <sessionName>                  = The session name that will be save in the database.")
     print("  -i | --interface <interfaceName>              = The interface name that will be used by airodump-ng.")
     print("")

if __name__ == '__main__':
     main()
