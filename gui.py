import commands

print """Hello, dear users.
We are the designers of this application.
This app to protect your personal information and your privacy.
We believe that it is your own rights.
Talk in real-time is dangerous, so it is mail mode in default.
Of course, you can add add-ons to make it diverse.
Enjoy, and be safe.
"""

menu_text="""
Supported Options:
1.Check Mailbox
2.Send Mail
"""

input_tip="Type your command:"

def main():
	print menu_text
	while 1:
		print input_tip,
		command=raw_input()
		if command=='1':
			pass
		if command=='2':
			print commands.getoutput("python2.7 client.py "+"hello")

if __name__ == '__main__':
	main()