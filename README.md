<h1 align="left">
  <br>
  <span>airodb</span>
  <img src="https://i.imgur.com/fbmWZ8f.png" width="64" alt="airodb" style="vertical-align:middle">
  <br>
</h1>

A python project to persist the airodump-ng output to a mongo database

#### Version 1.0.0

## Installation

```bash
apt install -y python3.6 python3-pip git
git clone https://github.com/jeremydumais/airodb.git
cd airodb
pip3 install -r requirements.txt
```

## How to use it
```bash
python3 airodb/airodb.py -s "MySession" -i wlan0
```