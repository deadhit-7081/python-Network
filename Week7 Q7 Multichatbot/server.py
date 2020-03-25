import socket

s=socket.socket()
print('Socket Created')
s.bind(('localhost',9999))
s.listen(3)
print("Waiting for Connection")
c1, addr = s.accept()
c2, add2 = s.accept()

while True:
    var1 = c1.recv(1024).decode()
    print("Client1 :",var1)
    var2=input("Server :")
    c1.send(bytes(var2,'utf-8'))
    print('Waiting for another client to message...')
    var3 = c2.recv(1024).decode()
    print("Client2 :",var3)
    var2 = input("Server :")
    c2.send(bytes(var2, 'utf-8'))
