#  Store ports and their corresponding services in a dictionary and allow the user to query by port number.

ports_services = {
    80: "HTTP",
    443: "HTTPS",
    22: "SSH",
    53: "DNS",
    21: "FTP"
}

usr_input = int(input("Enter a port number: "))

if usr_input in ports_services:
    print(f"Service for port {usr_input}: {ports_services[usr_input]}")
else:
    print("Port not found in the dictionary.")