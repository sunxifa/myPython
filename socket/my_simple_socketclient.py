import socket

s = socket.socket()

# host = socket.gethostname()
host = '192.168.179.134'
port = 1234

s.connect((host, port))
print s.recv(1024)
