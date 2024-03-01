import socket
import sys
import re

ip = sys.argv[1]

common_banners = {
    'SSH': b'SSH',
    'HTTP': b'HTTP',
    'HTTPS': b'HTTPS',
    'FTP': b'FTP',
    'SMTP': b'SMTP',
    'POP3': b'POP3',
    'IMAP': b'IMAP',
    'Telnet': b'Telnet',
    'DNS': b'DNS',
    'MySQL': b'MySQL',
}

def get_banner(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            banner = s.recv(1024)
            return banner
    except socket.error:
        return b''

def identify_service(banner):
    for service, banner_pattern in common_banners.items():
        if banner_pattern in banner:
            return service
    return None

for port in range(65535):
    banner = get_banner(ip, port)
    service = identify_service(banner)
    if service:
        print(f'[OPEN] Port {port}: {service}')
