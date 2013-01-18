from config.Configuration import Configuration
from lib.actions.Move import Move

class Mover(object):
  """"""
  screen = None
  # Valeurs temporaires, ca dependra du terrain, de la bestioles etc
  color = 255, 240, 200
  color_black = 0, 0, 0
  
  def __init__(self, screen):
    self.screen = screen
  
  def move(self, object_to_move):
    
    # TODO: L'appel vers la rfeflexion du brain devra etre ailleur,
    # ici on ne regardera que si l'action en cours est un deplacement
    # TODO: Attention, si on sort de la carte on fait un boucle infinie avec movePixel la
    action = object_to_move.brain.think()
    if (isinstance(action, Move)):
      self.uncolorizePixel(object_to_move.trace[object_to_move.length-1])
      object_to_move.updateTrace(self.movePixel(object_to_move.trace[0], action.direction))
      self.colorizePixel(object_to_move.trace[0])
  
  def uncolorizePixel(self, position):
    self.changePixel(position, self.color_black)
  
  def colorizePixel(self, position):
    self.changePixel(position, self.color)
  
  def changePixel(self, position, color):
    self.screen.set_at(position, color)
  
  
  def movePixel(self, pos, direction):
    x = pos[0]
    y = pos[1]
    
    if direction == 0:
      x = x+1
    if direction == 1:
      x = x+1
      y = y+1
    if direction == 2:
      y = y+1
    if direction == 3:
      x = x-1
      y = y+1
    if direction == 4:
      x = x-1
    if direction == 5:
      x = x-1
      y = y-1
    if direction == 6:
      y = y-1
    if direction == 7:
      x = x+1
      y = y-1
    
    if x < 0 or y < 0 or x > Configuration.CONF_SCREEN_WIDTH or y > Configuration.CONF_SCREEN_HEIGHT:
      return (320, 240)
    else:
      return (int(x), int(y))