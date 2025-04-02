# Write a function that takes a hostname and resolves it to an IP address.

import socket

hostname = input("Enter a Hostname: ")
def resolve_hostname(host):
    print(f'The {host} IP Address is {socket.gethostbyname(host)}')
resolve_hostname(hostname)