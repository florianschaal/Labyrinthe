#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

"""Fournit les infos du jeu"""

#Infos utiles au fonctionnement normal
port = 12348
separator = '\\'
path = "cartes/"
msg_jouer = 'c'
msg_fin = 'Bye'

#Infos physiques
robot_joueur = 'X'
robot_autre = 'x'
mur = 'O'
porte_libre = '.'
porte_close = ':'
sortie = 'U'
vide = ' '
obstacles = [robot_autre, mur, porte_close]
non_obstacles = [robot_joueur, porte_libre, sortie, vide]

#Infos d'instructions pour le robot
nord = 'n'
sud = 's'
est = 'e'
ouest = 'o'
murer = 'm'
percer = 'p'
directions = [nord, sud, est, ouest]
actions = [murer, percer]
