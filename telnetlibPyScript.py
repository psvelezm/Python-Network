# nano pythonR1script1

//----------

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

tn.write("enable\n")
tn.write("cisco\n")
tn.write("configure terminal\n")
tn.write("int loop 0\n")
tn.write("ip address 1.1.1.1 255.255.255.255\n")

tn.write("router ospf 1\n")
tn.write("network 0.0.0.0 255.255.255.255 area 0\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()   //display R1 the commands on ubuntu

//----------
//R1# debug telnet  //to see the script telneting to R1

//# python pythonR1script1
//PV
//password: cisco

//sh ip int brief
//sh run
