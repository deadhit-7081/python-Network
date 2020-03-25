import socket

c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
var=input("Client :")
c.sendto(var.encode('utf-8'),('localhost',9999))
print("Server :",var)
