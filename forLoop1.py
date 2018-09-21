// # nano pythonS1script1

// ----------

import getpass
import sys
import telnetlib

HOST = "192.168.122.71"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass() 

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")   //username prompt
tn.write (user + "\n")
if password:
	tn.read_until("Password: ")
	tn.write(password + "\n")

tn.write("configure terminal\n")

for n in range (2,10):				//// (2,21)
	tn.write("vlan" + str(n) + "\n")
	tn.write("name Python_Vlan_" + str(n) "\n")



tn.write("end\n")
tn.write("exit\n")

print tn.read_all()   //display R1 the commands on ubuntu
// ----------
// R1# debug telnet  //to see the script telneting to R1

// # python pythonS1script1
// pv
// password: cisco

// sh ip int brief
// sh run

