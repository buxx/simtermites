from math import sqrt

class Zone(object):
  
  id = ''
  position = None
  radius = 0
  draw = False
  draw_width = 1
  color = None
  
  def __init__(self, position, radius, zone_id):
    self.position = position
    self.radius = radius
    self.id = zone_id
  
  def positionIsInArea(self, tested_position):
    
    if sqrt((tested_position[0] - self.position[0]) ** 2 + (tested_position[1] - self.position[1]) ** 2) < self.radius:
      return True
    return False
