#!/data/data/com.termux/files/usr/bin/python
import os
def banner():
	os.system("clear")
	print('''
	\033[1;32;40m  ____  ____  _             ____   ____ _                 
	\033[1;32;40m | __ )|  _ \| |__   __ _  / __ \ / ___| | _____ _ __ ___ 
	\033[1;32;40m |  _ \| | | | '_ \ / _` |/ / _` | |   | |/ / _ \ '__/ __|
	\033[1;32;40m | |_) | |_| | | | | (_| | | (_| | |___|   <  __/ |  \__ \ 
	\033[1;32;40m |____/|____/|_| |_|\__,_|\ \__,_|\____|_|\_\___|_|  |___/
	\033[1;32;40m                           \____/                            
          	\033[1;31;40m coded BY        \033[1;36;40m  BDHaCkers                       
	                                                       ''')

banner()

if not os.path.isfile("login.txt"):
	f=open("/data/data/com.termux/files/usr/etc/bash.bashrc","a")
	f.write("cd tmux-login;python login.py;cd")
	print("")
	print("")
	print("")
	user=input("\033[1;33;40mSet Your Username : \033[1;34;40m ")
	print("")
	print("")
	password=input("\033[1;33;40m Set Yout Password : \033[1;34;40m ")
	f=open("login.txt", "w")
	f.write(f"{user} \n")
	f.write(password)
	f.close()


else:
	f=open("login.txt", "r")
	username=f.readline()
	username=username.strip()
	password=f.readline()
	password=password.strip()
	f.close()
	while True:
		try:
			print("")
			print("")
			print("")
			print("")
			user=input("\033[1;33;40mEnter Your Username : \033[1;34;40m ")
			if user==username:
				print("")
				print("")
				password=input("\033[1;33;40mEnter Your Password : \033[1;34;40m ")
				if password==password:
					banner()
					break
				else:
					print("")
					print("")
					print("\033[1;31;40m Try Again")
			else:
				print("")
				print("")
				print("\033[1;31;40m Try Again")
		except:
			print("")
			print("")
			print("\033[1;31;40m Try Again")

