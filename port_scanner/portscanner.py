"""
1. PortScanner is a program that allows you to scan target machine and discover if it has any open or closed ports
2. The main challenge is how can we discover if a port is open or not. Using a PortScanner we can see if we are able
   to connect to a certain port or not. If we are able to connect, then the port is open else the port is closed.
"""

import socket


def ipRangeList(ipRange):
    index = len(ipRange) - len(ipRange.split('.', 3)[-1]) - 1
    '''Finding the index of last dot(.) Reference taken for index (len(fullString) - len(sep[-1]) - len(subString), 
       where sep = fullString.split(subString, nthOccurrence)) 
    '''
    prefix = ipRange[:index + 1]
    start, end = list(map(int, ipRange[index + 1:].split("-")))
    return [prefix+str(suffix) for suffix in list(range(start, end+1))]


def ip(target):
    try:
        ipAddress = socket.gethostbyname(target)
        return ipAddress
    except:
        return None


def getBanner(s):
    return s.recv(1024).decode().strip('\n')


def scanPorts(ipAddr, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipAddr, port))
        try:
            banner = getBanner(sock)
            print(f"[+] Port {port} is Open : {banner}")
        except:
            print(f"[+] Port {port} Is Open")
    except:
        pass


def scan(ipList):
    if not isinstance(ipList, list):
        ipList = [ipList]
    print(ipList)
    for IP in ipList:
        target = ip(IP)
        if target is None:
            print(f"Invalid Target")
            return
        else:
            print(f"[-_0 Scanning Target] {IP}({target})")
            for port in range(0, 500):
                scanPorts(target, port)
            print()


if __name__ == "__main__":
    targets = input(f"[+] Enter IP/Domain: ")
    if "-" in targets:
        scan(ipRangeList(targets))
    else:
        scan(list(targets.replace(" ", "").split(",")))
