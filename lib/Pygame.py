import sys
try:
  import pygame
  from pygame.locals import *
except ImportError, err:
  print "Impossible de charger le module: %s" % (err)
  sys.exit(2)

# TODO: Utiliser de vrai constantes (cf google)
CONF_WINDOWS_NAME = 'Termites Simulator'
CONF_SCREEN_WIDTH = 640
CONF_SCREEN_HEIGHT = 480
CONF_TERMITES_COUNT = 1000

class Pygame(object):
  
  screen = None
  clock = None
  
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode((CONF_SCREEN_WIDTH, CONF_SCREEN_HEIGHT))
    pygame.display.set_caption(CONF_WINDOWS_NAME)
    background = pygame.Surface(self.screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    self.screen.blit(background, (0, 0))
    pygame.display.flip()
    self.clock = pygame.time.Clock()
  
  def display_update(self):
    pygame.display.update()