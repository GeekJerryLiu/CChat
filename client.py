import socket
import sys
s=socket.socket()
#connect
try:
	s.connect(('127.0.0.1', 8000))
	#get keyboard input
	s.sendall("0"+sys.argv[1])
	s.close()
	print "Sent Successfully."
except socket.error,e:
	print "[CChat] Cannot connect to remote server."
