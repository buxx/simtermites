# TODO: nettoyer les imports une fois le fichier propre
import sys
try:
  import pygame
  from pygame.locals import *
  from collections import deque
except ImportError, err:
  print "Impossible de charger le module. %s" % (err)
  sys.exit(2)
  
from lib.mover.Mover import Mover
from lib.Pygame import Pygame
from lib.simulation.SimulationManager import SimulationManager

# TODO: Utiliser de vrai constantes (cf google)
CONF_WINDOWS_NAME = 'Termites Simulator'
CONF_SCREEN_WIDTH = 640
CONF_SCREEN_HEIGHT = 480
CONF_TERMITES_COUNT = 1000

class Core(object):
  """"""
  
  pygame = None
  simulation = None
  
  def start(self):
    self.initialize_pygame()
    self.initialyze_simulation()
    
    while 1:
      # TODO: Ceci ira dans un gestionnaire d'evenement
      for event in pygame.event.get():
        if event.type == QUIT:
            return
      
      self.simulation.runCycle()
      
  def initialize_pygame(self):
    self.pygame = Pygame()
    
  def initialyze_simulation(self):
    self.simulation = SimulationManager(self)
