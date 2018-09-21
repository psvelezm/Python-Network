# nano pythonS1script1

----------

#!/usr/bin/env python

import getpass
import sys
import telnetlib

#Ask for username and password
user = raw_input("Enter telnet username:")
password = getpass.getpass()

#Open  a file called myswitches
f = open('myswitches')

#Telnet to switches and get the running config  
for line in f:   	
	print "Getting running config from Switch" + (line)
	HOST = line.strip()
	tn = telnetlib.Telnet(HOST)
	
	tn.read_until("Username:")
	tn.write(user + "\n")
	if password:
		tn.read_until("Password:")
		tn.write(password + "\n")
		
	tn.write("terminal length 0\n")
	tn.write("show run\n")
	tn.write("exit\n")

	readoutput = tn.read_all()
	saveoutput = open("switch" + HOST, "w")
	saveoutput.write(readoutput)
	saveoutput.close
