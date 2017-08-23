#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

"""Provide class Maps"""

import os
from ..setup import *

class Maps:
	"""Permet de choisir une carte parmi toutes celles présentes"""	
	
	def __init__(self):
		"""Récupération des cartes présentes"""
		self.cartes = os.listdir(path)
		self.carteChoisie = ""
		
	def show(self):
		"""Affiche toutes les cartes disponibles"""
		print("Labyrinthes existants :")
		index = 0
		for carte in self.cartes:
			index += 1
			carte = carte[:-3]
			print(str(index) + " - " + carte)
		print("")
		self.choose()
		
	def choose(self):
		"""Choix de la carte par l'utilisateur, avec gestion des erreurs"""
		while self.carteChoisie == "":
			try:
				choix = int(input("Entrez un numéro de labyrinthe pour commencer à jouer : "))
			except:
				self.carteChoisie = ""
			else:
				if choix <= 0 or choix > len(self.cartes):
					self.carteChoisie = ""
				else:
					self.carteChoisie = self.cartes[choix - 1]
