import socket

s=socket.socket()
print('Socket Created')
s.bind(('localhost',9999))
s.listen(3)
print("Waiting for Connection")
c, addr = s.accept()
while True:

    var=c.recv(1024).decode()
    if(var == 'exit'):
        c.close()
    else:
        print("Client :",var)
        var1=input("Server :")
        c.send(bytes(var1,'utf-8'))
