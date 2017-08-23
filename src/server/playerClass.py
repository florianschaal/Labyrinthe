#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

"""Provide Player class"""

from ..setup import *
import random

class Player:
	"""Pour avoir toutes les infos sur un joueur, dont son propre robot"""
	
	def __init__(self, client, infos, robot, pseudo = ""):
		"""Construction de la classe, pseudo facultatif"""
		self.client = client
		self.infos = infos
		self.robot = robot
		self.pseudo = pseudo
		
	def getIP(self):
		"""Obtenir IP client"""
		return self.infos[0]
		
	def getPort(self):
		"""Obtenir le port de com"""
		return self.infos[1]
		
	def sendMap(self, carte):
		"""Envoi de la carte avec joueur, en changeant l'avatar du joueur"""
		carte.update(self.robot.coord['x'], self.robot.coord['y'], robot_joueur)
		self.client.send(("\n" + carte.carteAEcrire + "\n" + separator).encode())
		carte.update(self.robot.coord['x'], self.robot.coord['y'], robot_autre)
		
	def sendMessage(self, message):
		"""Permet l'envoi d'un message formaté"""
		self.client.send((message + separator).encode())
		
	def close(self):
		"""Pour mettre fin à la co"""
		self.client.close()
