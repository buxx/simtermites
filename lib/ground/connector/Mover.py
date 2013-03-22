class Mover(object):
  """"""
  simulation = None
  # TODO: Valeurs temporaires, ca dependra du terrain, de la bestioles etc
  color_black = 0, 0, 0
  
  def __init__(self, simulation):
    self.simulation = simulation
  
  def move(self, object_to_move, move):
    if (move.direction != None):
      self.uncolorizePixel(object_to_move.trace[object_to_move.length-1])
      object_to_move.updateTrace(move.new_coordonates)
      
    first_position = True
    for position_trace in object_to_move.trace:
      color = self.getColorForContext(first_position, object_to_move)
      first_position = False
      self.colorizePixel(position_trace, color)
  
  def getColorForContext(self, first_position, object_to_move):
    if first_position:
      if hasattr(object_to_move, 'object_carried'):
        if object_to_move.object_carried != None:
          return object_to_move.object_carried.color
    return object_to_move.color
  
  def uncolorizePixel(self, position):
    self.colorizePixel(position, self.color_black)
    
  def colorizePixel(self, position, color):
    self.simulation.core.pygame.colorizer.colorizePixel(position, color)
