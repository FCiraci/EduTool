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

	def display_intro(self):
		print(self.logo)
		print(Fore.GREEN + f"		         Bienvenue {self.username} ! " + Style.RESET_ALL)
		print(Fore.RED + "		  	 © Copyright Furkan Ciraci \n\n\n" + Style.RESET_ALL)
		print("⚠ CE N'EST PAS UN TOOL POUR ATTAQUER VOUS NE RECUPEREZ QUE VOS PROPRES INFORMATIONS ⚠\n\n")
		print("Commande :")
		print("1 : Récuperer les informations systèmes")
		print("2 : Afficher le nom de l'utilisateur")
		print("3 : Récuperer votre adresse IP")
		print("4 : Pinger une adresse IP distante")

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
						adresse_ip = socket.gethostbyname(self.username)
						print(f"Votre adresse IP est : {adresse_ip}")
					case 4:
						ip_distant = input("Entrez l'adresse IP à pinger : ")
						ping_time = ping(ip_distant)
						if ping_time is None:
							print(f"Le ping vers {ip_distant} a échoué.")
						else:
							print(f"Le ping vers {ip_distant} a réussi avec un temps de {ping_time} secondes.")
			except ValueError:
				print("Veuillez entrer un nombre entier valide.")
			except KeyboardInterrupt:
				print("\n\nMerci d'avoir utilisé mon tool ! (CTRL-C appuyé)")
				break


if __name__ == "__main__":
	app = EduTool()
	app.display_intro()
	app.run()
