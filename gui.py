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

def send(text,code):
	"""
	CODE
	0 Normal Text
	1 System Setting
	"""
	if code==0:
		commands.getoutput("python2.7 client.py "+'0'+text)
	if code==1:
		commands.getoutput("python2.7 client.py "+'1'+text)

def main():
	username=raw_input("Set your username:")
	send(username,1)
	print menu_text
	while 1:
		print input_tip,
		command=raw_input()
		if command=='1':
			pass
		if command=='2':
			send("hello",0)

if __name__ == '__main__':
	main()