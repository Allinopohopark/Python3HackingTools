import portscanner


def solve(s, str, n):
    sep = s.split(str, n)
    if len(sep) <= n:
        return -1
    return len(s) - len(sep[-1]) - len(str)


ip = 'scanme.nmap.org'
portscanner.scan(ip)
