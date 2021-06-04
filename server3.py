import socket as skt

s_445 = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
host_445 = skt.gethostname()
port_445 = 9999
s_445.bind((host_445, port_445))
s_445.listen(5)

while True:
    conn_445, addr_445 = s_445.accept()
    str1 = conn_445.recv(1024).decode()
    if str1 == 'ping':
        print("SERVER PINGED")
        conn_445.send('pong'.encode())
    s_445.close()
