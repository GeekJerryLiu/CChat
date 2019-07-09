import socket

s=socket.socket()

#set a connection
s.bind(('127.0.0.1',8000))

#listen to requests
s.listen(1)

userinfo=[]
user_quantity=0
usermsgs=[]


#send messages to server
def send(text,code):
	"""
	CODE
	0 Normal Text
	1 System Setting
	"""
	#call client.py to send
	if code==0:
		#call in this way might be dangerous, it will be fixed in next large upgrade.
		commands.getoutput("python2.7 client.py "+'0'+text)
	if code==1:
		commands.getoutput("python2.7 client.py "+'1'+text)

while True:
    #wait for connecting
    conn,addr=s.accept()
    msg=conn.recv(1024)
    if msg!="":
    	#classify
        if msg[0]=='0':
        	#format: [TEXT][IP] CONTENT
            print '[TEXT]'+'['+addr[0]+'] '+msg[1:]
        if msg[0]=='1':
        	if msg[1:3]=='01':
        	#format: User Registered : USERNAME
        		print 'User Registered : '+msg[3:]
        		userinfo.append(msg[3:])
        		user_quantity+=1
        		print 'Now we have '+str(user_quantity)+' users in total.'
        	if msg[1:3]=='02':
        		send(userinfo[user_quantity],1)

            
s.close()