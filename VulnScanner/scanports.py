import socket


class ScanPorts:

    def __init__(self, target, port_boundary):
        self.target = target
        self.port_boundaries = port_boundary
        self.banners = []
        self.open_ports = []

    def _check_ip(self):
        try:
            return socket.gethostbyname(self.target)
        except:
            return None

    def scan_port(self, port):
        try:
            converted_ip = self._check_ip()
            if converted_ip is None:
                print("[-] Given IP/Domain is not valid!")
                return
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
            except:
                self.banners.append("")
            sock.close()
        except:
            pass

    def scan(self):
        for port in range(1, self.port_boundaries):
            self.scan_port(port)
