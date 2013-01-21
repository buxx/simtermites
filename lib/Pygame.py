import sys
from config.Configuration import Configuration
from lib.ground.Colorizer import Colorizer
try:
  import pygame
  from pygame.locals import *
except ImportError, err:
  print "Impossible de charger le module: %s" % (err)
  sys.exit(2)

class Pygame(object):
  
  screen = None
  colorizer = None
  clock = None
  event = None
  
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((Configuration.CONF_SCREEN_WIDTH, Configuration.CONF_SCREEN_HEIGHT))
    pygame.display.set_caption(Configuration.CONF_WINDOWS_NAME)
    background = pygame.Surface(self.screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    self.screen.blit(background, (0, 0))
    pygame.display.flip()
    self.clock = pygame.time.Clock()
    self.event = pygame.event
    self.colorizer = Colorizer(self.screen)
  
  def display_update(self):
    pygame.display.update()