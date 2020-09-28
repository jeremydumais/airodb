from dumpLoader import DumpLoader
from optionParser import OptionParser
from dbStorage import DBStorage
import os
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
from os import path


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   "hkds:vi:v",
                                   ["help", "session=", "interface=", "version", "debug", "keepdump"])
    except getopt.GetoptError as err:
        print(f"{Fore.RED}{str(err)}{Style.RESET_ALL}")
        displayUsage()
        sys.exit(2)
    optionParser = OptionParser(opts)
    validateRequiredArgs(optionParser)
    sessionName = optionParser.GetOptionValue("-s", "--session")
    interfaceName = optionParser.GetOptionValue("-i", "--interface")
    debugMode = optionParser.IsOptionExist("-d") or optionParser.IsOptionExist("--debug")
    keepDump = optionParser.IsOptionExist("-k") or optionParser.IsOptionExist("--keepdump")
    ensureAirodumpIsInstalled()
    ensureInterfaceExist(interfaceName)
    storage = DBStorage()
    ensureSessionNameDoesNotExist(storage, sessionName)

    # Launch the airodump-ng process
    filename = "dump-"+datetime.now().strftime("%Y%m%d%H%M%S")
    dumpFilename = filename + "-01.csv"
    airodumpCommand = ("sudo airodump-ng " + interfaceName +
                       " --output-format csv --write-interval 10 --manufacturer --uptime --write " +
                       filename + " > /dev/null 2>&1")
    try:
        print("Starting the airodump-ng process. Press CTRL+C when you want to stop...")
        process = subprocess.Popen(airodumpCommand, shell=True, stdin=subprocess.PIPE,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        timeElapsed = 0
        # Enter the main loop to process the dumps
        while True:
            time.sleep(0.1)
            timeElapsed = timeElapsed + 1
            if (timeElapsed > 20 and path.exists(dumpFilename)):
                dumps = DumpLoader.Load(dumpFilename, sessionName, debugMode)
                dumpsToAdd = []
                # Check if the dump already exist
                for dump in dumps:
                    if (storage.isEntryExist(dump) is False):
                        dumpsToAdd.append(dump)
                        if (debugMode):
                            print("New dump: " + json.dumps(dump))
                    if (len(dumpsToAdd) > 0):
                        storage.insert(dumpsToAdd)
                        print(len(dumpsToAdd), end="", flush=True)
                    else:
                        print(".", end="", flush=True)
                    timeElapsed = 0
    except KeyboardInterrupt:
        process.send_signal(signal.SIGINT)
    if (not keepDump and path.exists(dumpFilename)):
        os.remove(dumpFilename)


def validateRequiredArgs(optionParser):
    sessionFound = False
    interfaceFound = False
    if (optionParser.IsOptionExistAndValueIsNotEmpty("-s")
            or optionParser.IsOptionExistAndValueIsNotEmpty("--session")):
        sessionFound = True
    if (optionParser.IsOptionExistAndValueIsNotEmpty("-i")
            or optionParser.IsOptionExistAndValueIsNotEmpty("--interface")):
        interfaceFound = True
    if (optionParser.IsOptionExist("-h")
            or optionParser.IsOptionExist("--help")):
        displayUsage()
        sys.exit(0)
    if (optionParser.IsOptionExist("--version")):
        displayVersion()
        sys.exit(0)
    if not sessionFound or not interfaceFound:
        displayUsage()
        sys.exit(2)


def displayUsage():
    print("Usage: airodb --session <sessionName> --interface <interfaceName> [ optionalArgs ]")
    print("Required arguments:")
    print("  -s | --session <sessionName>             = The session name that will be save in the database.")
    print("  -i | --interface <interfaceName>         = The interface name that will be used by airodump-ng.")
    print("")
    print("Optional arguments:")
    print("  -d | --debug                             = Display debug information during the execution.")
    print("  -k | --keepdump                          = Do not delete the dump file when the application exit.")
    print("  -h | --help                              = Display the help (this message) and exit.")
    print("  --version                                = Display version information and exit.")
    print("")


def displayVersion():
    print("airodb - version " + getVersion())
    print("Created by Jeremy Dumais")
    print("https://github.com/jeremydumais/airodb")


def getVersion():
    return "1.0.0"


def ensureAirodumpIsInstalled():
    print("Looking for airodump-ng binary...            ", end=" ", flush=True)
    airodumpBinaryPath = distutils.spawn.find_executable("airodump-ng")
    if (airodumpBinaryPath is None):
        print(f"{Fore.RED}Error{Style.RESET_ALL}")
        print(f"{Fore.RED}The airodump-ng doesn't seem to be installed!{Style.RESET_ALL}")
        print("Please refer to https://www.aircrack-ng.org/install.html for the installation instructions.")
        exit(2)
    else:
        print(f"{Fore.GREEN}Done{Style.RESET_ALL}")


def ensureInterfaceExist(interfaceName):
    print("Validating the network interface...          ", end=" ", flush=True)
    interfaces = psutil.net_if_addrs()
    if (interfaceName not in interfaces):
        print(f"{Fore.RED}Error{Style.RESET_ALL}")
        print(f"The interface {interfaceName} doesn't seem to exist!")
        print("Please confirm that the interface is detected and that it is configured in monitor mode.")
        exit(2)
    else:
        print(f"{Fore.GREEN}Done{Style.RESET_ALL}")


def ensureSessionNameDoesNotExist(storage, sessionName):
    if (storage.isSessionNameAlreadyExist(sessionName)):
        print(f"{Fore.RED}The session {sessionName} already exist!{Style.RESET_ALL}")
        exit(2)


if __name__ == '__main__':
    main()
