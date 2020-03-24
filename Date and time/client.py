import socket

c=socket.socket()

c.connect(('localhost',9999))
name=input("Enter Your Name :")
c.send(bytes(name,'utf-8'))
print("Date :",c.recv(1024).decode())