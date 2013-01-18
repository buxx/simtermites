import pygame
from pygame.locals import *

class EventManager(object):
  
  core = None
  
  def __init__(self, Core):
    self.core = Core
  
  # TODO: A terme on ecoute ici les event, puis on agit sur les objets
  # par le biais de self.core.machin
  def listenAndPropagate(self):
    for event in self.core.pygame.event.get():
      if event.type == QUIT:
        return false
    return True