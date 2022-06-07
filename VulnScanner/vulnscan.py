from VulnScanner import scanports

targetIp = input("[+] Target: ")
portBoundary = int(input("[+] Enter PortBoundary(Default: 1-500): "))
vuln_file = input("[+] Enter path of VulnFile: ")
print()

scanner = scanports.ScanPorts("scanme.nmap.org", portBoundary)
scanner.scan()

with open(vuln_file, 'r') as file:
    count = 0
    for banner in scanner.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print(f"[+] Vulnerable Banner: '{banner}' ON PORT : '{scanner.open_ports[count]}'")
        count += 1
