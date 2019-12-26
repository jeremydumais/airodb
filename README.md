# airodb

## Description
A python project to persist the airodump-ng output to a mongo database

#### Version 1.0.0
##### *All the instructions below are for Ubuntu 18.04. It is currently the only OS that airodb has been tested on.

## Installation

```bash
sudo apt install -y python3.6 python3-pip git
git clone https://github.com/jeremydumais/airodb.git
cd airodb
sudo pip3 install -r requirements.txt
```

## How to use it
```bash
python3 airodb/airodb.py -s "MySession" -i wlan0
```

## How it works

<img src="https://raw.githubusercontent.com/jeremydumais/airodb/medias/airodbRunningExample.gif">

First you must run airodb/airodb.py file with the two required arguments : session (-s or --session) and interface (-i or --interface)

The application will then start the airodump-ng process and will log in a file dump-\<current date time\>-01.csv in the root of the airodb project folder.

airodb will then look in that file every two seconds to see if there is new AP's or if already seen AP's have new values.

It will write a dot if nothing is new or it will display a number to indicate how many AP's was new or changed.

Note : The unicity of a line in the database is based on the four following fields : SessionName, BSSID, FirstTimeSeen and LastTimeSeen. It means that you will have multiple lines in the database for an AP in a session. You can then compute some statistics for example the Power average of an AP during a session etc.



## Prerequisite

### Install MongoDB
```bash
sudo apt install mongodb
```

#### Ensure the MongoDB service is running
```bash
sudo systemctl status mongodb
```
<img src="https://raw.githubusercontent.com/jeremydumais/airodb/medias/mongoDBRunning.png" alt="ifconfigExample">

#
### Install aircrack-ng
```bash
sudo apt install aircrack-ng
```
#

### Prepare your network interface interface

#### Get the name of your wireless interface
```bash
ifconfig
```
> Example
<img src="https://raw.githubusercontent.com/jeremydumais/airodb/medias/interfaces.png" alt="ifconfigExample">

#### Put the interface down, set to monitor mode and bring it up
```bash
ifconfig wlxa0ab1b3b52a2 down
iwconfig wlxa0ab1b3b52a2 mode monitor
ifconfig wlxa0ab1b3b52a2 up
```

## Program arguments
### Required arguments
| Switches | Description |
| -------|:--------|
| -s, --session | The session name that will be save in the database. |
| -i, --interface | The session name that will be save in the database. |

### Optional arguments
| Switches | Description |
| -------|:--------|
| -d, --debug | Display debug information during the execution. |
| -k, --keepdump | Do not delete the dump file when the application exit. |
| -h, --help | Display the help and exit. |
| --version | Display version information and exit. |

#

*The logo are a construction from images made by Freepik and Smashicons from www.flaticon.com*