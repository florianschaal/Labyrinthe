#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

"""Programme principal du labyrinthe"""

from src.server.serverClass import *
from src.setup import *

hote = ''

#On choisit la carte
cartes = Maps()
cartes.show()
carte = Map(cartes.carteChoisie)
carte.load()
#On définit le serveur
server = Server(hote, port, carte)
#On attend les joueurs
server.waitPlayers()
#On joue
server.play()
#On ferme!
server.close()
