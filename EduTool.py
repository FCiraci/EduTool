from colorama import *
import os
import socket

init(autoreset=True)

class EduTool:
    def __init__(self):
        self.logo = """ 
  _______  ________   ____  ____  ___________  ______      ______    ___       
 /"     "||"      "\\ ("  _||_ " |("     _   ")/    " \\    /    " \\  |"  |      
(: ______)(.  ___  :)|   (  ) : | )__/  \\\\__/// ____  \\  // ____  \\ ||  |      
 \\/    |  |: \\   ) ||(:  |  | . )    \\\\_ /  /  /    ) :)/  /    ) :)|:  |      
 // ___)_ (| (___\\ || \\\\ \\__/ //     |.  | (: (____/ //(: (____/ //  \\  |___   
(:      "||:       :) /\\\\ __ //\\     \\:  |  \\        /  \\        /  ( \\_|:  \\  
 \\_______)(________/ (__________)     \\__|   \\"_____/    \\"_____/    \\_______) 
																			  
"""
        self.username = os.getlogin()

    def display_intro(self):
        print(self.logo)
        print(Fore.GREEN + f"		         Bienvenue {self.username} ! " + Style.RESET_ALL)
        print(Fore.RED + "		  	 © Copyright Furkan Ciraci" + Style.RESET_ALL)
        print("⚠ CE N'EST PAS UN TOOL POUR ATTAQUER VOUS NE RECUPEREZ QUE VOS PROPRES INFORMATIONS ⚠")
        print("Commande :")
        print("1 : Récuperer les informations systèmes")
        print("2 : Afficher le nom de l'utilisateur")

    def run(self):
        while True:
            try:
                saisie = int(input("\nEntrez une commande : "))
                match saisie:
                    case 1:
                        print(os.uname())
                    case 2:
                        print(self.username)
                    case _:
                        print("Action inconnue, veuillez saisir une valeur présente ci-dessus")
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")


if __name__ == "__main__":
    app = EduTool()
    app.display_intro()
    app.run()
