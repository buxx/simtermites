#!/usr/bin/python
# coding: utf-8

import sys
try:
  import pygame
  from pygame.locals import *
  import random
  from collections import deque
except ImportError, err:
  print "Impossible de charger le module. %s" % (err)
  sys.exit(2)
  
CONF_SCREEN_WIDTH = 640
CONF_SCREEN_HEIGHT = 480
CONF_TERMITES_COUNT = 1000
  
class ObjectAlive(object):
  
  # La trace est l'historique des positions de l'objet
  # ASavoir: Bug si on initialise le deque ici et pas dans le __init__
  trace = None
  # Longeur de notre petite bête
  length = 2
  
  def __init__(self, pos, length):
    
    # On itinialise la trace
    self.trace = deque()
    self.length = length
    
    # Pour être serain on prépare une trace complète, je t'expliquerai poruquoi
    # quand on se verra c'est une astuce pour gagner en performance
    i = 1
    while i <= self.length:
      self.trace.appendleft(pos)
      i = i+1
      
  def updateTrace(self, pos):
    """ cette méthode ajoute la nouvelle position a l'historique des
    positions, puis limite la "taille" de l'historique à la longeur désiré
    """
    # appendleft permet de mettre la nouvelle position en début du tableau
    # ce qui décale les anciennes valeurs
    self.trace.appendleft(pos)
    # On elève toujours la dernière position historique de la trace, pour ne pas avoir un
    # tableau qui grossisse, grossisse ... et prenne toutte la ram !
    del self.trace[self.length]

class ObjectMover(object):
  """ Cet objet s'ocupue de déplacer un objet déplacable
  """
  screen = None
  color = 255, 240, 200
  color_black = 0, 0, 0
  
  def __init__(self, screen):
    self.screen = screen
  
  def move(self, object_to_move):
    
    # (screen.set_at permet de changer la couleur d'un pixel)
    
    # Premier point: colorier en noir le pixel de fin d'historique
    self.screen.set_at(object_to_move.trace[object_to_move.length-1], self.color_black)
    # On met a jour la position du pixel
    object_to_move.updateTrace(movePixel(object_to_move.trace[0]))
    self.screen.set_at(object_to_move.trace[0], self.color)

def movePixel(pos):
  """ C'est pour l'instant la seule représentation du cerveau d'une termite
  L'algorithme fonctionne sur une base simple: determiner une direction a prendre
  au hasard. Il y a 8 directions possibles:
  6 7 8
  5   1
  4 3 2
  """
  x = pos[0]
  y = pos[1]
  direction = random.randint(1, 8)
  if direction == 1:
    x = x+1
  if direction == 2:
    x = x+1
    y = y+1
  if direction == 3:
    y = y+1
  if direction == 4:
    x = x-1
    y = y+1
  if direction == 5:
    x = x-1
  if direction == 6:
    x = x-1
    y = y-1
  if direction == 7:
    y = y-1
  if direction == 8:
    x = x+1
    y = y-1
    
  # On fait ça a l'arrache mais si ca sort de l'écran de jeu, on recommence
  # il y aura une technique plus économe en ressource qui éviterai de relancer la foction a chaque fois
  # que la nouvelle valeur est en dehors. Tu peux essayer de trouver laquelle :p
  if x < 0 or y < 0 or x > CONF_SCREEN_WIDTH or y > CONF_SCREEN_HEIGHT:
    return movePixel(pos)
  else:
    return (int(x), int(y))

def getRandomPos():
  """ On genere juste un x,y pour placer les termites au hasard, enfin cette fonction
  ne fait que retourner un coordoné au hasard"""
  x = random.randint(0, CONF_SCREEN_WIDTH)
  y = random.randint(0, CONF_SCREEN_HEIGHT)
  return (x, y)

def main():
  
  #######
  ## Début bordel de code pour 2D
  ### Si tu pige pas tout ici c'est pas le plus important
  #######
  # Initialisation de la fenêtre d'affichage
  pygame.init()
  screen = pygame.display.set_mode((CONF_SCREEN_WIDTH, CONF_SCREEN_HEIGHT))
  pygame.display.set_caption('Termites Simulator')

  # Remplissage de l'arrière-plan
  background = pygame.Surface(screen.get_size())
  background = background.convert()
  background.fill((0, 0, 0))

  # Blitter le tout dans la fenêtre
  screen.blit(background, (0, 0))
  pygame.display.flip()
  clock = pygame.time.Clock()
  
  #######
  ## Fin bordel de code pour 2D
  #######

  # Ici on va générer les objets de nos x termites
  pixel_count = 1
  # On stocke nos termites dans le tableau "pixels"
  # oui je les ai appelé pixel dans ce code héhé
  pixels = []
  while pixel_count <= CONF_TERMITES_COUNT:
    pixels.append(ObjectAlive(getRandomPos(), 2))
    pixel_count = pixel_count+1
    
  # On prépare notre objet qui fait bouger les termites. Son seul argument
  # pour sa construction est "screen". Il en aura besoin pour redessiner les pixels
  mover = ObjectMover(screen)

  # Cette boucle est la base de toutes application de type jeux,
  # en faite on fait calculer le processeur tout le temps dans une boucle infinie
  # Dans notre cas chaque boucle sera en fait un cycle de calculs des déplacements
  # Tu te dis surement oula ca va calculer très vite pour un oeil humain: en effet, c'est pour ça
  # qu'on a le tick, tu verra juste en dessous
  while 1:
    
    ## Ces truc d'event permette de récupérer les touches, clicks etc
    for event in pygame.event.get():
        if event.type == QUIT:
            return
    
    # voilà notre affaire, pour chaque termites dans notre tableau
    for pixel in pixels:
      # On la fait bouger
      mover.move(pixel)
    
    # Ces trucs d'update et flip permette de "rafraichir" l'ecran. Il ne suffit pas de changer des
    # pixels il faut ensuite dire au truc qui gere l'ecran d'appliquer les changements
    pygame.display.update()
    #pygame.display.flip() # On utilise pas flip, enfin il y un truc d'optimisation que j'ai lu quelquepart, je t'en parlerais.
    
    # C'est cette methode tick qui permet de "rythmer" la vitesse des cycles.
    # Ici, ca veut dire 25 cycles par secondes.
    clock.tick(25)
    ##
 
# Ca je connais pas mais a mon avis ca lance notre tointoin dans main une fois que tout est pret
if __name__ == '__main__': main()