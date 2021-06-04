import socket


HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
FORMAT = 'utf-8'


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    entry = bytes((input("Enter the string: ").encode(FORMAT)))
    s.sendall(entry)
    data  = s.recv(1024).decode('UTF-8')

print(data)