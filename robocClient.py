#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

"""Programme principal du labyrinthe"""

from src.client.clientClass import *
from src.setup import *

#Infos serveur
hote = 'localhost'

#Création du client connecté au serveur spécifié
client = Client(hote, port)
client.connect()
client.run()


