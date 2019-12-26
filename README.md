<h1 align="center">
  <span>airodb</span>
  <br>
  <img src="https://i.imgur.com/fbmWZ8f.png" width="54" alt="airodb">
  <br>
</h1>

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

## Prerequisite

### Install MongoDB
```bash
sudo apt install mongodb
```

#### Ensure the MongoDB service is running
```bash
sudo systemctl status mongodb
```
#
### Install aircrack-ng
```bash
sudo apt install aircrack-ng
```
#
### Prepare your network interface interface

##### The logo are a construction from images made by Freepik and Smashicons from www.flaticon.com