#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

"""Provide class Map"""

import sys
import os
from ..setup import *

class Map:
	"""Fournit les outils nécessaires pour la traduction de la carte
			jouable <-> imprimable"""	
	
	def __init__(self, carte):
		"""Construction de l'objet"""
		self.nom = carte
		self.original = ""
		self.carte = []
		self.carteAEcrire = ""
		self.exitIsReached = False
					
	def load(self):
		"""Chargement de la carte"""
		if os.path.exists(path+self.nom):
			with open(path+self.nom, "r") as map:
				self.original = map.read()
			self.toTable()
			self.check()
		else:
			print("Carte non disponible")
			sys.exit(1)
			
	def check(self):
		"""Vérifie la conformité de la map"""
		for line in self.carte:
			for content in line:
				if content not in obstacles and content not in non_obstacles and content != '\n':
					print("Carte non conforme, chargement impossible")
					sys.exit(1)
			
	def toTable(self):
		"""Permet de remplir une table avec la chaîne récupérée"""
		buf = []
		for content in self.original:
			buf.append(content)
			if content == '\n':
				self.carte.append(buf)
				buf = []
			
	def getContent(self, x, y):
		"""Retourne le contenu de la case (copie)"""
		return list(self.carte[y])[x]
	
	def toString(self):
		"""Stockage du tableau dans une chaine de caracteres"""
		bufferCarte = []
		for content in self.carte:
			bufferCarte.append(''.join(content))
		self.carteAEcrire = ''.join(bufferCarte)
			
	def update(self, x, y, symbole):
		"""Ecriture dans la carte jouable, jointure avec le carte imprimable"""
		self.carte[y][x] = symbole
		self.toString()
