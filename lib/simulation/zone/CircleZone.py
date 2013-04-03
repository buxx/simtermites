from lib.simulation.zone.Zone import Zone
from math import sqrt

class CircleZone(Zone):
  
  position = None
  radius = 0
  draw_width = 1
  
  def __init__(self, position, radius, zone_id):
    Zone.__init__(self, zone_id)
    self.position = position
    self.radius = radius
  
  def positionIsInArea(self, tested_position):
    if self.getDistanceFromAreaCenter(tested_position) < self.radius:
      return True
    return False
  
  def getDistanceFromAreaCenter(self, tested_position):
    return sqrt((tested_position[0] - self.position[0]) ** 2 + (tested_position[1] - self.position[1]) ** 2)
