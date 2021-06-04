import socket


HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('connected by', addr)
        while True:
            data = conn.recv(1024).decode('UTF-8')
            if not data:
                break

            string1 = ("Message in Uppercase: " + data.upper())
            arr = bytes(string1, 'utf-8')
            conn.sendall(arr)