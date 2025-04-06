# Implement a script that finds live hosts on a local network.

from ping3 import ping 

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

print("Live hosts:")
for ip in range(0, 256):
    hostname = f"192.168.0.{ip}"
    delay = ping(hostname)

    if delay:
        print(f"{GREEN}{hostname} responded in {delay} seconds")
print(f"The operation is complete.{RESET}")