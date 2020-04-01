# Bulk Domain Availability Checking Tool

## Installation

### Requirements

-python3

-pip3

### Setup
> Install requirements first
```
$ pip3 install -r requirements.txt
```

### Usage
```
$ ./bdac.py
usage: bdac.py [-h] [--file FILE] [--domains DOMAINS [DOMAINS ...]] [--socket]
               [--whois]

optional arguments:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  Path to file containing domains
  --domains DOMAINS [DOMAINS ...], -d DOMAINS [DOMAINS ...]
                        List of domains
  --socket, -s          Use socket method for checking availability. Note: It
                        return available if it fails to resolve domain names
                        to their namesevers and unavailable if domain resolves
                        (It won't show grabbed domains that are available)
  --whois, -w           Use whois method for checking availability. Note:
                        There are limited tries an IP can have (No official
                        number but some estimate about 1000/day)
```
### Examples
```
Socket method and domains list
$ ./bdac.py -s -d google.com quora.com

Whois method and domains file
$ ./bdac.py -w -f domains.txt

Both methods and domains file
$ ./bdac.py -s -w -f domains.txt
```

### Note
Tested on Ubuntu 18.04

whois has about 1000 requests limit per day

### TODO
handle file path from different directory accross any os

ADD nslookup method

whois method is teerribly slow, try making it asynchronous
