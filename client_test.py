import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 6379))

# Test SET
s.send(b"SET user gemini\n")
print(s.recv(1024).decode())

# Test GET
s.send(b"GET user\n")
print(s.recv(1024).decode())