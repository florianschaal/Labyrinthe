#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

"""Programme principal du labyrinthe"""

from src.mapsClass import *
from src.mapClass import *
from src.robotClass import *
from src.setup import *
import socket
import select

hote = ''
port = 12345

#On définit le serveur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creation socket TCP
server.bind((hote, port)) #Bind sur port

cartes = Maps()
cartes.show()

carteUpdate = Map(cartes.carteChoisie)

server.listen(5) #Co max
joueurs = []
robotsJoueurs = []
accept = True
print("En attentes des joueurs...")

while accept:
	connexions_entrantes, wlist, xlist = select.select([server], [], [], 0.05)
	for connexion in connexions_entrantes:
		#On accepte les connexions
		joueur, infos_joueur = server.accept() #Accepte la co
		joueurs.append(joueur)	
		robot = Robot(carteUpdate.carte)
		robotsJoueurs.append(robot)
		print("Client IP " + joueur.getpeername()[0] + " port " + str(joueur.getpeername()[1]) + " connecté.")

	try:
		lireJoueurs, ecrireJoueurs, xlist = select.select(joueurs, joueurs, [], 0.05)
	except:
		pass
	else:
		for joueur in lireJoueurs:
			msg_recu = joueur.recv(1024) 
			if msg_recu == b"c":
				print("Partie lancée par : " + joueur.getpeername()[0] + " sur le port " + str(joueur.getpeername()[1]))
				accept = False
		for joueur in ecrireJoueurs:
			joueur.send(b"")
				
carteUpdate.toString()
#for j in joueurs:
	#j.send(carteUpdate.carteAEcrire.encode())

while False:
	commande = robot.getEntry()
	
	if commande != quitter:
		carteUpdate.update(robot)
		if robot.exit == True:
			print("Well done")
			break
	else:
		break


for joueur in joueurs:
	joueur.send(msg_fin.encode())
#	joueur.close()
#server.close()
while True:
	pass
