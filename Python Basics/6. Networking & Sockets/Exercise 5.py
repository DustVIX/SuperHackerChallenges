# Write a program that resolves a domain name to an IP address.

import socket

hostname = input("Enter a Hostname: ")
def resolve_hostname(host):
    print(f'The {host} IP Address is {socket.gethostbyname(host)}')
try:
    resolve_hostname(hostname)
except socket.gaierror:
    print("Sorry, domain not found")