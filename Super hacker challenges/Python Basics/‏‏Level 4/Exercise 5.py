# Write a function that checks if an IP address is valid.

ipv4 = input("Enter a IPv4 address: ")
def ip_checker(ip):
    arr_ip = ip.split(".")
    counter = 0
    for i in arr_ip:
        if len(i) < 4 and int(i) < 255:
            counter = counter + 1
    if counter == 4:
        print(f"The {ip} is a valid ip")
    else:
        print(f"The {ip} is not a valid ip")

ip_checker(ipv4)