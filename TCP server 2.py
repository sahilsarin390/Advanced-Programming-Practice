import socket
s = socket.socket()
host = socket.gethostname()
port = 9999
s.bind((host,port))
print('Server Running...')
s.listen(5)
while True:
    conn, addr = s.accept()
    print('Got Connection from ',addr)
    conn.send('Server is saying Hi')
    conn.close()