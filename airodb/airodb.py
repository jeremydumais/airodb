from dumpLoader import DumpLoader
from optionParser import OptionParser
from dbStorage import DBStorage
import distutils.spawn
import subprocess
import getopt
import sys
from colorama import Fore, Style
import psutil
import signal
import time
from datetime import datetime
import json

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
     ensureAirodumpIsInstalled()
     ensureInterfaceExist(interfaceName)
     storage = DBStorage()
     ensureSessionNameDoesNotExist(storage, sessionName)

     #Launch the airodump-ng process
     filename = "dump-"+datetime.now().strftime("%Y%m%d%H%M%S")
     airodumpCommand = ("sudo airodump-ng "+interfaceName+
          " --output-format csv --write-interval 10 --manufacturer --uptime --write "+
          filename+" > /dev/null 2>&1")
     try:
          process = subprocess.Popen(airodumpCommand, shell=True, stdout=subprocess.PIPE)
          timeElapsed = 0
          #Enter the main loop to process the dumps
          while True:
               time.sleep(0.1)
               timeElapsed = timeElapsed + 1
               if (timeElapsed > 50):
                    dumps = DumpLoader.Load(filename+"-01.csv", sessionName)
                    dumpsToAdd = []
                    #Check if the dump already exist
                    for dump in dumps:
                         if (storage.isEntryExist(dump) == False):
                              dumpsToAdd.append(dump)
                              print("New dump: " + json.dumps(dump))
                    if (len(dumpsToAdd) > 0):
                         storage.insert(dumpsToAdd)   
                    timeElapsed = 0
     except KeyboardInterrupt:
          process.send_signal(signal.SIGINT)


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

def ensureAirodumpIsInstalled():
     airodumpBinaryPath = distutils.spawn.find_executable("airodump-ng")
     if (airodumpBinaryPath == None):
          print(f"{Fore.RED}The airodump-ng doesn't seem to be installed!{Style.RESET_ALL}") 
          print("Please refer to https://www.aircrack-ng.org/install.html for the installation instructions.")
          exit(2)

def ensureInterfaceExist(interfaceName):
     interfaces = psutil.net_if_addrs()
     if (interfaceName not in interfaces):
          print(f"{Fore.RED}The interface {interfaceName} doesn't seem to exist!{Style.RESET_ALL}") 
          print("Please confirm that the interface is detected and that it is configured in monitor mode.")
          exit(2)

def ensureSessionNameDoesNotExist(storage, sessionName):
     if (storage.isSessionNameAlreadyExist(sessionName)):
          print(f"{Fore.RED}The session {sessionName} already exist!{Style.RESET_ALL}") 
          exit(2)

if __name__ == '__main__':
     main()
