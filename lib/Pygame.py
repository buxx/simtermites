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
  default_font = None
  
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
    self.default_font = pygame.font.SysFont("arial", 11)
  
  def display_update(self):
    pygame.display.update()
  
  def draw_rect(self, color, data, thickness):
    pygame.draw.rect(self.screen, color, data, thickness)
  
  def getLabel(self, text, color = (255,255,0)):
    return self.default_font.render(text, 1, color)