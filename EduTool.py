from colorama import *
import os
import socket
from ping3 import *

init(autoreset=True)

class EduTool:
	def __init__(self):
		self.logo = (Fore.YELLOW + """ 
  _______  ________   ____  ____  ___________  ______      ______    ___       
 /"     "||"      "\\ ("  _||_ " |("     _   ")/    " \\    /    " \\  |"  |      
(: ______)(.  ___  :)|   (  ) : | )__/  \\\\__/// ____  \\  // ____  \\ ||  |      
 \\/    |  |: \\   ) ||(:  |  | . )    \\\\_ /  /  /    ) :)/  /    ) :)|:  |      
 // ___)_ (| (___\\ || \\\\ \\__/ //     |.  | (: (____/ //(: (____/ //  \\  |___   
(:      "||:       :) /\\\\ __ //\\     \\:  |  \\        /  \\        /  ( \\_|:  \\  
 \\_______)(________/ (__________)     \\__|   \\"_____/    \\"_____/    \\_______) 
																			  
""" + Style.RESET_ALL)
		self.username = os.getlogin()

	def check_sudo(self):
		if os.geteuid() != 0:
			print(Fore.RED + "Ce programme nécessite les privilèges sudo pour fonctionner.")
			print("Veuillez le relancer avec sudo : `sudo python3 EduTool.py`" + Style.RESET_ALL)
			exit()


	def display_intro(self):
		print(self.logo)
		print(Fore.GREEN + f"		         Bienvenue {self.username} ! " + Style.RESET_ALL)
		print(Fore.RED + "		  	 © Copyright Furkan Ciraci \n\n\n" + Style.RESET_ALL)
		print("Commande :")
		print("1 : Récuperer les informations systèmes")
		print("2 : Afficher le nom de l'utilisateur")
		print("3 : Récuperer votre adresse IP")
		print("4 : Pinger une adresse IP distante")
  
  
	def get_ip(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		try:
			s.connect(('10.255.255.255', 1))
			IP = s.getsockname()[0]
		except:
			IP = '127.0.0.1'
		finally:
			s.close()
		print(f"Votre adresse IP est : {IP}")


	def ping_adresse(self):
		ip_distant = input("Entrez l'adresse IP à pinger : ")
		ping_time = ping(ip_distant)
		if ping_time is None:
			print(f"Le ping vers {ip_distant} a échoué.")
		else:
			print(f"Le ping vers {ip_distant} a réussi avec un temps de {ping_time} secondes.")
   

	def run(self):
		while True:
			try:
				saisie = int(input("\nEntrez une commande : "))
				match saisie:
					case 1:
						print(os.uname())
					case 2:
						print(self.username)
					case 3:
						self.get_ip()
					case 4:
						self.ping_adresse()
			except ValueError:
				print("Veuillez entrer un nombre entier valide.")
			except KeyboardInterrupt:
				print("\n\nMerci d'avoir utilisé mon tool ! (CTRL-C appuyé)")
				break


if __name__ == "__main__":
	app = EduTool()
	app.check_sudo()
	app.display_intro()
	app.run()
 