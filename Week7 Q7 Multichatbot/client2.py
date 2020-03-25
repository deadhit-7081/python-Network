import socket

c2=socket.socket()

c2.connect(('localhost',9999))
while True:
    name=input("Client2 :")
    c2.send(bytes(name,'utf-8'))
    print("Server :",c2.recv(1024).decode())
