import random

# TODO: Utiliser de vrai constantes (cf google)
CONF_WINDOWS_NAME = 'Termites Simulator'
CONF_SCREEN_WIDTH = 640
CONF_SCREEN_HEIGHT = 480
CONF_TERMITES_COUNT = 1000

class Mover(object):
  """"""
  screen = None
  color = 255, 240, 200
  color_black = 0, 0, 0
  
  def __init__(self, screen):
    self.screen = screen
  
  def move(self, object_to_move):
    
    self.screen.set_at(object_to_move.trace[object_to_move.length-1], self.color_black)

    object_to_move.updateTrace(self.movePixel(object_to_move.trace[0]))
    self.screen.set_at(object_to_move.trace[0], self.color)
  
  # TODO L'intelligence de deplacement devra etre dans des objets qui reponde aux
  # specificites des objets deplaces
  def movePixel(self, pos):
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
    
    if x < 0 or y < 0 or x > CONF_SCREEN_WIDTH or y > CONF_SCREEN_HEIGHT:
      return self.movePixel(pos)
    else:
      return (int(x), int(y))