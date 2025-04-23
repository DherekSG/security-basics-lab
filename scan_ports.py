import socket

def scan_ports(host):
    print(f"Scanning {host}...")
    for port in range(20, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Porta {port} aberta")
        s.close()

scan_ports("127.0.0.1")
