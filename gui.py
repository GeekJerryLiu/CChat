import commands

print """Hello, dear users.
We are the designers of Shambhala.
Shambhala is used to protect your personal information and your privacy.
Of course, you can add add-ons to make Shambhala more and more diverse.
We believe in the world, we can find a place just like Shambhala, pure and glorious.
Enjoy, and be safe.

May God and Buddha bless us.
"""

menu_text="""
Supported Options:
1.Check Mailbox
2.Send Mail
"""

input_tip="Type your command:"

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
		commands.getoutput("python2.7 client.py "+'101'+text)
def recieve():
	rec_addr,rec_msg=commands.getoutput("python2.7 receive.py ")
	return rec_addr,rec_msg
	

def main():
	username=raw_input("Set your username:")
	#send username to server for log
	send(username,1)
	print menu_text
	while True:
		print input_tip,
		command=raw_input()
		if command=='1':
			pass
		if command=='2':
			#There should be a interface like vim or nano that user can type words in it. it's a hard work.
			#at the moment, you can only send one-line messages.
			msg=raw_input("Type your words(ends with a enter): ")
			send('\"'+msg+'\"',0)
		if command=='3':
			print receive()

if __name__ == '__main__':
	main()