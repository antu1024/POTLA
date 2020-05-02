
from pyfiglet import Figlet
import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
		print("Invaalid Amount of arguments.")
		print("Syntax: Python3 scanner.py <IP>")
custom_fig = Figlet(font='big')
print(custom_fig.renderText('  POTLA'))
print("================================================================")
print("= DEVELOPER: ARMAN HOSSAIN ANTU // ANTU1024                    =")
print("= TWITTER  : https://twitter.com/antu1024                      =")
print("= ABOUT IT : POTLA is a Port Scanning Tool                     =")
print("================================================================")
print("")

print("="* 50)
print("Scanning target "+target)
print("Time Started: "+str(datetime.now()))
print("="* 50)

print("[@] 1// Scanning All Port")
print("[@] 2// Scanning just selected Port")
print("[@] 3// Quit")
print("================================================================")
selection=int(input("[#] Select your Mode (1,2,3):>> "))
print("================================================================")
if selection==1:
	try: 
		for port in range (1,65535):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target,port)) 
			#print("Checking port {}".format(port))
			if result == 0:
				print("==========================")
				print(" [+] Port {} is open".format(port))
				print("==========================")
				s.close()
		print("================================================================")
		print("")
		print("== Copyright 2020 'C' By ARMAN HOSSAIN ANTU // ANTU1024        =")
		print("")
		print("================================================================")
	except KeyboardInterrupt:
		print("\nExiting program.")
		print("================================================================")
		print("")
		print("== Copyright 2020 'C' By ARMAN HOSSAIN ANTU // ANTU1024        =")
		print("")
		print("================================================================")
		sys.exit()
	except socket.gaierror:
		print("Hostname could not be resolved.")
		print("================================================================")
		print("")
		print("== Copyright 2020 'C' By ARMAN HOSSAIN ANTU // ANTU1024        =")
		print("")
		print("================================================================") 
		sys.exit()
	except socket.error:
		print("couldn't connect to server.")
		print("================================================================")
		print("")
		print("== Copyright 2020 'C' By ARMAN HOSSAIN ANTU // ANTU1024        =")
		print("")
		print("================================================================")
		sys.exit()
elif selection==2:
	try:
		a = int(input("[*]Scanning Port From : "))
		b = int(input("[*]Scanning Port To   : "))
		for port in range (a,b):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target,port)) 
			#print("Checking port {}".format(port))
			if result == 0:
				print("==========================")
				print(" [+] Port {} is open".format(port))
				print("==========================")
				s.close()
		print("================================================================")
		print("")
		print("== Copyright 2020 'C' By ARMAN HOSSAIN ANTU // ANTU1024        =")
		print("")
		print("================================================================")
	except KeyboardInterrupt:
		print("\nExiting program.")
		print("================================================================")
		print("")
		print("== Copyright 2020 'C' By ARMAN HOSSAIN ANTU // ANTU1024        =")
		print("")
		print("================================================================")
		sys.exit()
	except socket.gaierror:
		print("Hostname could not be resolved.")
		print("================================================================")
		print("")
		print("== Copyright 2020 'C' By ARMAN HOSSAIN ANTU // ANTU1024        =")
		print("")
		print("================================================================") 
		sys.exit()
	except socket.error:
		print("couldn't connect to server.")
		print("================================================================")
		print("")
		print("== Copyright 2020 'C' By ARMAN HOSSAIN ANTU // ANTU1024        =")
		print("")
		print("================================================================")
		sys.exit()
	
elif selection==3:
	exit()
	
else:
	print("================================================================")
	print("")
	print("== Invalid Mode. Enter 1-3. :))                                =")
	print("")
	print("================================================================")
	print("================================================================")
	print("")
	print("== Copyright 2020 'C' By ARMAN HOSSAIN ANTU // ANTU1024        =")
	print("")
	print("================================================================") 
