#!/usr/bin/python
# example:
# > python fuzz.py test.txt

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
import sys

import smtplib

filename = sys.argv[1]
with open(filename, 'r') as myfile:
	data = myfile.read()

data2 = data.split("\n\n")

toWhom = 'target@target.com' # mail address to test
username = 'username@mail.com' # your mail address
password = 'pawwsord' # your mail password

def sendMail(subject, data):

	fromaddr = username
	toaddrs = toWhom

	server = smtplib.SMTP('smtp.example.com:587') # smtp tls server and port
	server.starttls()
	server.login(username,password)

	text = "fail"

	msg = MIMEMultipart('alternative')
	msg['Subject'] = subject
	msg['From'] = fromaddr
	msg['To'] = toaddrs
	part1 = MIMEText(text, 'plain')
	part2 = MIMEText(data, 'html')

	msg.attach(part1)
	msg.attach(part2)

	server.sendmail(fromaddr, toaddrs, msg.as_string())
	server.quit()

count = 0

for i in data2:
	count += 1
	sendMail(str(count),i)

with open("re", 'r') as myfile:
        numbers = myfile.read().split("\n")


# Кусок кода для проверки номера у пэйлоада:
#for i in data2:
#	count += 1
#	for x in numbers:
#		if x == str(count):
#			print "\n"
#			print i

