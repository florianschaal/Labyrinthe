#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

"""Provide class Server"""

from .mapsClass import *
from .mapClass import *
from .robotClass import *
from .playerClass import *
from ..setup import *
import socket
import select
import sys

class Server:
	"""Crétion du serveur de jeu"""
	
	def __init__(self, hote, port, map):
		"""Bind du serveur si possible"""
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			self.server.bind((hote, port))
		except:
			print("Port non disponible")
			sys.exit(1)

		self.carte = map

		self.joueurs = []
		self.accept = True
		
	def waitPlayers(self):
		"""Attente des joueurs, fin si message de début de partie reçu"""
		self.server.listen(5)
		print("En attentes des joueurs...\n")
		while self.accept:
			self.getConnexions()
			msg_recu = self.getMessages()
			for msg in msg_recu:
				if msg['msg'] == msg_jouer:
					print("\nPartie lancée par " + msg['exp'].getIP() + ":" + str(msg['exp'].getPort()))
					self.accept = False
					self.broadcastMessage("La partie commence !\n")
					self.broadcastMap()
		self.server.close()
								
	def getConnexions(self):
		"""Accept des connexions entrantes, envoi des premiers messages"""
		co_entrantes, wlist, xlist = select.select([self.server], [], [], 0.05)
		for co in co_entrantes:
			client, infos_client = self.server.accept()
			robot = Robot()
			robot.place(self.carte.carte)
			player = Player(client, infos_client, robot)
			self.joueurs.append(player)
			print("Client connecté (" + player.getIP() + ":" + str(player.getPort()) + ")")
			player.sendMessage("Bienvenue joueur " + str(len(self.joueurs)) + "\n") 
			player.sendMap(self.carte)
			player.sendMessage("Entrez '" + msg_jouer + "' pour lancer la partie :\n")
	
	def getMessages(self):
		"""Récupération en parallèle des messages de tous les joueurs.
			Les messages seront des dicos avec le message et l'expéditeur"""
		clients = []
		msg = {}
		msg_recu = []
		for joueur in self.joueurs:
			clients.append(joueur.client)
		try:
			read, wlist, xlist = select.select(clients, [], [], 0.05)
		except:
			pass
		else:
			for joueur in read:
				msg['msg'] = ''.join(joueur.recv(1024).decode().split(separator))
				for i in self.joueurs:
					if joueur == i.client:
						msg['exp'] = i
				msg_recu.append(msg)
		return msg_recu
				
	def close(self):
		"""Fermeture des co, envoi du message de fin"""
		for joueur in self.joueurs:
			joueur.sendMessage(msg_fin)
			joueur.close()
		
		
	def broadcastMessage(self, message):
		"""Envoi d'un message à tous les joueurs"""
		for joueur in self.joueurs:
			joueur.sendMessage(message)
			
	def broadcastMap(self):
		"""Envoi de la map à tous les joueurs"""
		for joueur in self.joueurs:
			joueur.sendMap(self.carte)
		
	def play(self):
		"""Phase de jeu"""
		nextPlayer = True
		instr = ""
		index = 0
		
		while not self.carte.exitIsReached:
			#Si c'est au joueur suivant
			if nextPlayer:
				#On prend le focus sur lui
				joueur = self.joueurs[index]
				#On calcule le prochain joueur
				if index == (len(self.joueurs) - 1):
					index = 0
				else:
					index += 1
				#On informe les joueurs
				self.broadcastMessage("C'est au joueur " + str(self.joueurs.index(joueur)+1) + " de jouer\n")
				nextPlayer = False
			#On reçois tous les messages
			msg_recu = self.getMessages()
			#Si l'expéditeur est le joueur en cours
			for msg in msg_recu:
				if msg['exp'] == joueur:
					instr = msg['msg']
					break
			#Si aucune action en cours, on récupère celle du joueur
			if joueur.robot.nbMove == 0 and not joueur.robot.percer and not joueur.robot.murer:
				joueur.robot.getInstruction(instr)
			#Sinon, le robot agit
			else:
				joueur.robot.act(self.carte)
				#Après action, on renvoit la map
				self.broadcastMap()
				#On regarde si le joueur a atteint la sortie
				if joueur.robot.exit:
					#Message de fin, fermeture du jeu
					self.broadcastMessage("Le joueur " + str(self.joueurs.index(joueur)+1) + " a atteint la sortie !\n\n")
					print("Partie finie par " + joueur.getIP() + ":" + str(joueur.getPort()))
					self.carte.exitIsReached = True
				#Sinon, c'est au joueur suivant
				else:
					nextPlayer = True
			#RAZ de l'instruction reçue
			instr = ""
				
				
			
