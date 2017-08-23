#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

"""Provide class ReadWrite"""

from threading import Thread, Event
from ..setup import *
import sys
from io import StringIO

stop = Event()

class ReadWrite(Thread):
	"""Permet de lire et écrire en parallèle, sur 2 threads"""
	
	def __init__(self, serveur, mode):
		"""Construction, mode 'r' ou 'w'"""
		Thread.__init__(self)
		self.serveur = serveur
		self.mode = mode
			
	def run(self):
		"""Tant que l'event n'est pas levé"""
		while not stop.isSet():
			if self.mode == 'r':
				self.read()
			elif self.mode == 'w':
				self.write()
		
	def read(self):
		"""On lit le serveur, on lève l'event si on reçoit le message de fin"""
		msg_recu = self.serveur.recv(1024).decode() 
		liste_msg_recu = msg_recu.split(separator)
		for msg in liste_msg_recu:
			if msg == msg_fin:
				stop.set()
				sys.stdout.write("Appuyez sur 'Entrée' pour quitter...")
				sys.stdout.flush()
			else:
				sys.stdout.write(msg)
				sys.stdout.flush()
		
	def write(self):
		"""On écrit sur le serveur si l'event n'est pas levé. La fonction readline() étant bloquante, le joueur doit appuyer sur entrée pour quitter"""
		msg_send = sys.stdin.readline()
		if not stop.isSet():
			self.serveur.send((msg_send[:-1] + separator).encode())
