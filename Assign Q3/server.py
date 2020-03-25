import socket

s = socket.socket()
print('Socket Created')
s.bind(('localhost',9999))
s.listen(3)
print('Waiting for Connection')
while True:
    c, addr = s.accept()
    var=c.recv(1024).decode()
    print('Client :',var)
    if(var == 'ping'):
        c.send(bytes('pong','utf-8'))
    c.close()
