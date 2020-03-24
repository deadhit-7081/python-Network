import socket
import datetime

s=socket.socket()

print('Socket Created')

s.bind(('localhost', 9999))
s.listen(3)
print('waiting for connection')
while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected with", addr ,name)
    str=datetime.datetime.now()
    x=str.strftime("%X")
    c.send(bytes(x , 'utf-8'))
    c.close()
