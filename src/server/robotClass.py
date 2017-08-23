#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

"""Provide class Robot"""

from ..setup import *
import random

class Robot:
	"""Permet de jouer avec le robot sur une carte"""
	
	def __init__(self):
		"""Définition initiale de tous ses attributs"""
		self.coord = {}
		self.newCoord = {}
		self.direction = ''
		self.nbMove = 0
		self.murer = False
		self.percer = False
		self.exit = False
		self.under = vide
		
	def place(self, carte):
		"""Placement aléatoire sur case vide"""
		#On fait un placement random jusqu'à tomber sur une case vide
		y = random.randint(0, len(carte)-2)
		x = random.randint(0, len(carte[0])-1)
		while carte[y][x] != vide:
			y = random.randint(0, len(carte)-2)
			x = random.randint(0, len(carte[0])-1)
		#On place le robot sur cette case, on lui donne les coord
		carte[y][x] = robot_autre
		self.coord = {'x' : x, 'y' : y}
		
	def act(self, carte):
		"""Méthode à appeler pour faire agir le robot"""
		if self.nbMove != 0:
			self.move(carte)
		elif self.percer == True:
			self.drill(carte)
		elif self.murer == True:
			self.wall(carte)
		
	def getInstruction(self, instr):
		"""Décodage de l'instruction"""
		#Réinitialisation des actions
		self.nbMove = 0
		self.murer = False
		self.percer = False
		
		#Si le joueur rentre une commande
		if len(instr) != 0:
			#Si il s'agit d'un déplacement valide
			if instr[0] in directions:
				#On récupère, si besoin, le nb de déplacement
				if len(instr) != 1:
					try:
						self.nbMove = int(instr[1:])
					except:
						return
				else:
					self.nbMove = 1
				#On place le robot dans la bonne direction
				self.direction = instr[0]
			#Si il s'agit d'une action spéciale
			elif instr[0] in actions:
				if len(instr) != 2:
					return
				#Si la commande est valide
				if instr[1] in directions:
					#On récupère l'action
					if instr[0] == murer:
						self.murer = True
					elif instr[0] == percer:
						self.percer = True
					else:
						return
					#On place le robot dans la bonne direction
					self.direction = instr[1]
				else:
					return
			else:
				return
				
	def newCoordonnates(self):
		"""Calcul des nouvelles coordonnées en fonction des actuelles"""
		self.newCoord = dict(self.coord)
		if self.direction == sud:
			self.newCoord['y'] += 1
		elif self.direction == nord:
			self.newCoord['y'] -= 1
		elif self.direction == ouest:
			self.newCoord['x'] -= 1
		elif self.direction == est:
			self.newCoord['x'] += 1

	def drill(self, carte):
		"""Permet de percer une porte"""
		self.newCoordonnates()
		if carte.getContent(self.newCoord['x'], self.newCoord['y']) != porte_close:
			return
		carte.update(self.newCoord['x'], self.newCoord['y'], porte_libre)
		self.percer = False
		
	def wall(self, carte):
		"""Permet de murer une porte"""
		self.newCoordonnates()
		if carte.getContent(self.newCoord['x'], self.newCoord['y']) != porte_libre:
			return
		carte.update(self.newCoord['x'], self.newCoord['y'], porte_close)
		self.murer = False
			
	def move(self, carte):
		"""Bouge le robot sur la carte en se basant sur la carte initiale"""
		self.newCoordonnates()
		#On récupère le contenu de la case sur laquelle le robot agit
		new = carte.getContent(self.newCoord['x'], self.newCoord['y'])
		#Si la case est diponible pour bouger
		if new not in obstacles:
			#Le robot se déplace
			carte.update(self.coord['x'], self.coord['y'], self.under)
			carte.update(self.newCoord['x'], self.newCoord['y'], robot_autre)
			self.under = new
			self.coord = dict(self.newCoord)
		#Si on atteint la sortie
		if self.under == sortie:
			self.exit = True
		#Un mouvement est fait
		self.nbMove -= 1

	
