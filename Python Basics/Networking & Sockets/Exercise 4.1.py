#  Create a simple client-server program using socket.

import socket

host = "127.0.0.1"
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))
client.send(b"HI")
response = client.recv(1024)
print(response)