import socket

s=socket.socket()

#set a connection
s.bind(('127.0.0.1',8000))

#listen to requests
s.listen(1)

#wait for connecting
conn,addr=s.accept()
msg=conn.recv(1024)

print addr
print msg