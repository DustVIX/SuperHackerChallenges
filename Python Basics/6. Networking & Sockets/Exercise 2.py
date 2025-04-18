# Use socket to scan open ports on scanme.nmap.org for ports 20-100.

import socket

target_hosts = input("Enter the host IP address: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))


def scan_ports(host_port, start_port, end_port):
    print(f"Scanning ports on {host_port}...")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set a connection timeout

        result = sock.connect_ex((host_port, port))

        if result == 0:
            print(f"Port {port} is open")

        sock.close()

scan_ports(target_hosts, start_port, end_port)