#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

"""Test class Map"""

import unittest
from src.server.mapClass import *
from src.setup import *

class MapTest(unittest.TestCase):
	"""Tests des objets de la classe Map"""

	def setUp(self):
		"""Construction d'une carte virtuelle"""
		self.map = Map("Test")
		self.map.carte = [	[mur,mur,mur], 
							[mur,vide,mur], 
							[mur,mur,mur]]
		self.map.original = mur+vide+porte_libre+'\n'+mur+robot_autre+porte_close+'\n'
		
	def tearDown(self):
		"""A appeler à la fin du test"""
		pass
	
	def test_toString(self):
		"""Test pour afficher la carte en chaine de caractères"""
		self.map.toString()
		self.assertEqual(self.map.carteAEcrire, mur+mur+mur+mur+vide+mur+mur+mur+mur)
		
	def test_update(self):
		"""Test pour changer une case de la map"""
		self.map.update(0, 1, vide)
		self.assertEqual(self.map.carte, [[mur,mur,mur],[vide,vide,mur],[mur,mur,mur]])
		
	def test_getContent(self):
		"""Test pour récupération d'une case"""
		content = self.map.getContent(0, 0)
		self.assertEqual(content, mur)
		
	def test_toTable(self):
		"""Test pour convertir la chaîne de caractère en tableau utilisable"""
		self.map.carte = []
		self.map.toTable()
		self.assertEqual(self.map.carte, [[mur, vide, porte_libre, '\n'], [mur, robot_autre, porte_close, '\n']])
