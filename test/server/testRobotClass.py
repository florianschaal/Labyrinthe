#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

"""Test class Robot"""

import unittest
from src.server.robotClass import *
from src.server.mapClass import *
from src.setup import *

class RobotTest(unittest.TestCase):
	"""Tests des objets de la classe Robot"""

	def setUp(self):
		"""Construction d'un robot"""
		self.robot = Robot()
		
	def tearDown(self):
		"""A appeler à la fin du test"""
		pass
	
	def test_place(self):
		"""Test de placement aléatoire du robot, ici obligatoirement dans la seule case vide"""
		map = [	[mur,mur,mur], 
				[mur,vide,mur], 
				[mur,mur,mur]]
		self.robot.place(map)
		self.assertEqual(self.robot.coord['x'], 1)
		self.assertEqual(self.robot.coord['y'], 1)
		
	def test_getIntruction(self):
		"""Test de plusieurs instructions"""
		#Direction nord, sans ajouter de nb de coups
		self.robot.getInstruction(nord)
		self.assertEqual(self.robot.direction, nord)
		self.assertEqual(self.robot.nbMove, 1)
		self.assertFalse(self.robot.murer)
		self.assertFalse(self.robot.percer)
		#Direction sud, sur 10 coups
		self.robot.getInstruction(sud+'10')
		self.assertEqual(self.robot.direction, sud)
		self.assertEqual(self.robot.nbMove, 10)
		self.assertFalse(self.robot.murer)
		self.assertFalse(self.robot.percer)
		#Construction de mur
		self.robot.getInstruction(murer+est)
		self.assertEqual(self.robot.direction, est)
		self.assertEqual(self.robot.nbMove, 0)
		self.assertTrue(self.robot.murer)
		self.assertFalse(self.robot.percer)
		#Une autre instruction non conforme, on garde la direction d'avant
		self.robot.getInstruction("Autre")
		self.assertEqual(self.robot.direction, est)
		self.assertEqual(self.robot.nbMove, 0)
		self.assertFalse(self.robot.murer)
		
	def test_drill(self):
		"""Test de percage d'une porte"""
		#Si la porte n'est pas une porte close
		map = Map("test")
		map.carte = [[vide,vide,porte_close]]
		self.robot.coord['x'] = 0
		self.robot.coord['y'] = 0
		self.robot.direction = est
		self.robot.drill(map)
		self.assertEqual(map.carte, [[vide,vide,porte_close]])
		#Si la porte est une porte close
		map = Map("test")
		map.carte = [[vide,vide,porte_close]]
		self.robot.coord['x'] = 1
		self.robot.coord['y'] = 0
		self.robot.direction = est
		self.robot.drill(map)
		self.assertEqual(map.carte, [[vide,vide,porte_libre]])
		
	def test_wall(self):
		"""Test de murage d'une porte"""
		#Si la porte n'est pas une porte libre
		map = Map("test")
		map.carte = [[vide,vide,porte_libre]]
		self.robot.coord['x'] = 0
		self.robot.coord['y'] = 0
		self.robot.direction = est
		self.robot.wall(map)
		self.assertEqual(map.carte, [[vide,vide,porte_libre]])
		#Si la porte est une porte libre
		map = Map("test")
		map.carte = [[vide,vide,porte_libre]]
		self.robot.coord['x'] = 1
		self.robot.coord['y'] = 0
		self.robot.direction = est
		self.robot.wall(map)
		self.assertEqual(map.carte, [[vide,vide,porte_close]])
		
	def test_newCoordonates(self):
		"""Test du calcul des nouvelles coord"""
		self.robot.coord['x'] = 1
		self.robot.coord['y'] = 0
		self.robot.direction = ouest
		self.robot.newCoordonnates()
		self.assertEqual(self.robot.newCoord, {'x':0, 'y':0})
		
	def test_move(self):
		"""Test de déplacement du robot"""
		#Si le déplacement est possible
		map = Map("test")
		map.carte = [[vide,robot_autre,porte_libre]]
		self.robot.under = porte_libre
		self.robot.coord['x'] = 1
		self.robot.coord['y'] = 0
		self.robot.direction = est
		self.robot.nbMove = 1
		self.robot.move(map)
		self.assertEqual(self.robot.nbMove, 0)
		self.assertEqual(map.carte, [[vide,porte_libre,robot_autre]])
		#Si un obstacle
		map = Map("test")
		map.carte = [[vide,robot_autre,porte_close]]
		self.robot.under = porte_libre
		self.robot.coord['x'] = 1
		self.robot.coord['y'] = 0
		self.robot.direction = est
		self.robot.nbMove = 1
		self.robot.move(map)
		self.assertEqual(self.robot.nbMove, 0)
		self.assertEqual(map.carte, [[vide,robot_autre,porte_close]])
