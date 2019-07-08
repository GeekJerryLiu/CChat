import socket
s=socket.socket()

#set a connection
s.bind(('127.0.0.1',8000))

#listen to requests
s.listen(1)

while 1:
    #wait for conncting
    conn,addr=s.accept()
    msg=conn.recv(1024)
    if msg!="":
        if msg[0]=='0':
            print '[TEXT]'+'['+addr[0]+'] '+msg[1:]
        if msg[0]=='1':
        	print 'User Registered : '+msg[1:]
            
s.close()