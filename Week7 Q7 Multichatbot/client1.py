import socket

c1=socket.socket()

c1.connect(('localhost',9999))
while True:
    name=input("Client1 :")
    c1.send(bytes(name,'utf-8'))
    print("Server :",c1.recv(1024).decode())
