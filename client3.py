import socket as skt

c_445= skt.socket()
host_445 = skt.gethostname()
port_445 = 9999
c_445.connect((host_445,port_445))

c_445.send('ping'.encode())
str2 = c_445.recv(1024).decode()
if str2 == 'pong':
    print('CLIENT PONGED')