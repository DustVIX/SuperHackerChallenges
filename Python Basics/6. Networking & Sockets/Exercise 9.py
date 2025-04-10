# Write a program that pings a list of IPs and prints their status.

from ping3 import ping 

list_ips = ["192.168.0.1","192.168.0.149","192.168.0.197","192.168.0.244","192.168.0.2","192.168.0.44"]

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"


print("Live hosts:")
for ip in list_ips:
    delay = ping(ip)

    if delay:
        print(f"{GREEN}{ip} responded in {delay} seconds{RESET}")
    else:
        print(f"{RED}{ip} did not respond{RESET}")
print("")