import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket Created')

s.bind(('localhost',9999))
print('Waiting for Connection')
while True:
    var , addr =s.recvfrom(1024)
    var_str=var.decode('utf-8')
    s.sendto(var_str.encode(),addr)
