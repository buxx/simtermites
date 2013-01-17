# TODO: nettoyer les imports une fois le fichier propre
import sys
try:
  import pygame
  from pygame.locals import *
  from collections import deque
except ImportError, err:
  print "Impossible de charger le module. %s" % (err)
  sys.exit(2)
  
from lib.entity.bug.termite.Worker import Worker as TermiteWorker
from lib.mover.Mover import Mover

# TODO: Utiliser de vrai constantes (cf google)
CONF_WINDOWS_NAME = 'Termites Simulator'
CONF_SCREEN_WIDTH = 640
CONF_SCREEN_HEIGHT = 480
CONF_TERMITES_COUNT = 1000

class Core(object):
  """"""
  # TODO: Mettre pygame dans un objet maison, ainsi que ses attributs
  screen = None
  clock = None
  
  # TODO: ce tableau sera gere par un objet de gestion de la simulation. En tout cas pas dans Core
  termites = []
  
  # Le mover aussi sera inclu dans l'objet de la simulation, cf juste au dessus
  mover = None
  
  def start(self):
    self.initialize_pygame()
    self.initialyze_simulation()
    
    while 1:
      
      # TODO: Ceci ira dans un gestionnaire d'evenement
      for event in pygame.event.get():
          if event.type == QUIT:
              return
      
      # TODO: Ca bougera dans l'objet simulation
      for termite in self.termites:
        self.mover.move(termite)
      
      pygame.display.update()
      self.clock.tick(25)
      
  def initialize_pygame(self):
    pygame.init()
    self.screen = pygame.display.set_mode((CONF_SCREEN_WIDTH, CONF_SCREEN_HEIGHT))
    pygame.display.set_caption(CONF_WINDOWS_NAME)
    background = pygame.Surface(self.screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    self.screen.blit(background, (0, 0))
    pygame.display.flip()
    self.clock = pygame.time.Clock()
    
  def initialyze_simulation(self):
    termites = 1
    self.termites = []
    while termites <= CONF_TERMITES_COUNT:
      self.termites.append(TermiteWorker((20, 20)))
      termites = termites+1
    self.mover = Mover(self.screen)
  