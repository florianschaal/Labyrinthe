#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

"""Provide class Client"""

from ..setup import *
from .readwriteClass import *
import sys
import socket

class Client:
	"""Créé un client connecté au serveur"""

	def __init__(self, hote, port):
		"""Création du socket"""
		self.hote = hote
		self.port = port
		self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creation socket TCP

	def connect(self):
		"""Si le serveur écoute, on s'y connecte"""
		print("Tentative de connexion au serveur...")
		try:
			self.server.connect((self.hote, self.port)) #On connecte au serveur
		except:
			print("Serveur non disponible.")
			sys.exit(1)
		print("Connexion établie avec le serveur.\n")
		
	def run(self):
		"""On lit et écrit en parallèle sur le serveur"""
		ecriture = ReadWrite(self.server, 'w')
		lecture = ReadWrite(self.server, 'r')
		ecriture.start()
		lecture.start()
		ecriture.join()
		lecture.join()
		self.server.close()
