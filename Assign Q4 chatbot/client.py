import socket

c=socket.socket()

c.connect(('localhost',9999))
while True:
    name=input("Client :")
    c.send(bytes(name,'utf-8'))
    print("Server :",c.recv(1024).decode())
