"""
1. PortScanner is a program that allows you to scan target machine and discover if it has any open or closed ports
2. The main challenge is how can we discover if a port is open or not. Using a PortScanner we can see if we are able
   to connect to a certain port or not. If we are able to connect, then the port is open else the port is closed.
"""

import socket
import sys


def ip(target):
    try:
        ipAddress = socket.gethostbyname(target)
        print(f"[-] IP address found: {ipAddress}")
        return ipAddress
    except:
        return None


def scanPorts(ipAddr, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipAddr, port))
        print(f"[+] Port {port} Is Open")
    except:
        # pass
        print(f"[-] Port {port} Is Closed")


target = ip(input("[+] Target IP/Domain: "))
ipaddress = target if target is not None else sys.exit("[-] Provided Target is Invalid!")
for port in range(1, 100):
    scanPorts(ipaddress, port)
