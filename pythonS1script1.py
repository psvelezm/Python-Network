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

tn.write("vlan 2\n")
tn.write("name Python_VLAN_2\n")

tn.write("exit\n")

tn.write("vlan 3\n")
tn.write("name Python_VLAN_3\n")
tn.write("exit\n")

tn.write("vlan 4\n")
tn.write("name Python_VLAN_4\n")
tn.write("exit\n")

tn.write("vlan 5\n")
tn.write("name Python_VLAN_5\n")
tn.write("exit\n")

tn.write("vlan 6\n")
tn.write("name Python_VLAN_6\n")
tn.write("exit\n")

tn.write("end\n")
tn.write("exit\n")

print tn.read_all()   //display R1 the commands on ubuntu

//----------
//R1# debug telnet  //to see the script telneting to R1

//# python pythonS1script1
//PV
//password: cisco

//sh ip int brief
//sh run
