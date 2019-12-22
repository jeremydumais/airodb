from dumpLoader import DumpLoader
from optionParser import OptionParser
from dbStorage import DBStorage
import getopt
import sys
from colorama import Fore, Style

def main():
     try:
          opts, args = getopt.getopt(sys.argv[1:],"hs:vi:v",["help","session=", "interface=", "version"])
     except getopt.GetoptError as err:
          print(f"{Fore.RED}{str(err)}{Style.RESET_ALL}")
          displayUsage()
          sys.exit(2)
     optionParser = OptionParser(opts)
     validateRequiredArgs(optionParser)
     sessionName = optionParser.GetOptionValue("-s", "--session")
     interfaceName = optionParser.GetOptionValue("-i", "--interface")
     storage = DBStorage()
     #Check if that session name already exist
     if (storage.isSessionNameAlreadyExist(sessionName)):
          print(f"{Fore.RED}The session {sessionName} already exist!{Style.RESET_ALL}") 
          exit(2)
     #Launch the airodump process
     
     #Enter the main loop to process the dumps
     dumps = DumpLoader.Load("dump/dump.csv", sessionName)
     #storage.insert(dumps)   


def validateRequiredArgs(optionParser):
     
     sessionFound = False
     interfaceFound = False
     if (optionParser.IsOptionExistAndValueIsNotEmpty("-s") 
     or optionParser.IsOptionExistAndValueIsNotEmpty("--session")):
          sessionFound = True
     if (optionParser.IsOptionExistAndValueIsNotEmpty("-i") 
     or optionParser.IsOptionExistAndValueIsNotEmpty("--interface")):
          interfaceFound = True
     if (optionParser.IsOptionExist("-h") or optionParser.IsOptionExist("--help")):
          displayUsage()
          sys.exit(0)
     if (optionParser.IsOptionExist("--version")):
          displayVersion()
          sys.exit(0)
     if not sessionFound or not interfaceFound:
          displayUsage()
          sys.exit(2)

#ParseOptionClass

def displayUsage():
     print("Usage: airodb --session <sessionName> --interface <interfaceName>")
     print("  -s | --session <sessionName>             = The session name that will be save in the database.")
     print("  -i | --interface <interfaceName>         = The interface name that will be used by airodump-ng.")
     print("  -h | --help                              = Display the help (this message) and exit.")
     print("  --version                                = Display version information and exit.")
     print("")

def displayVersion():
     print("airodb - version " + getVersion())
     print("Created by Jeremy Dumais")
     print("https://github.com/jeremydumais/airodb")

def getVersion():
     return "0.9.0"

if __name__ == '__main__':
     main()
