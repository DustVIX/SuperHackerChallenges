#  Create a simple client-server program using socket.

import socket

ServerIP = "127.0.0.1"
ServerPort = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ServerIP,ServerPort))
server.listen(3)
print(f"Listening on {ServerIP}:{ServerPort} ...")

def handle(client_soket):
    response = client_soket.recv(1024)
    print("Recv: ", response)
    client_soket.send(b"hi")
    client_soket.close()
while True:
    client , date = server.accept()
    print(f"Con form : {date[0]}:{date[1]}")
    handle(client)