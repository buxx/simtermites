from lib.simulation.zone.Zone import Zone
from math import sqrt

class TraceZone(Zone):
  
  coordonates = []
  width = 0
  
  def __init__(self, coordonates, width, zone_id):
    Zone.__init__(self, zone_id)
    
    new_coordonates = []
    current_step = 0
    
    while current_step <= len(coordonates)-1:
      new_coordonates.append(coordonates[current_step])
      current_step += width
    
    self.coordonates = new_coordonates
    self.width = width
  
  def positionIsInArea(self, tested_position):
    for coordonate in self.coordonates:
      if self.getDistanceFromPoint(tested_position, coordonate) < self.width:
        return True
    return False
  
  def getDistanceFromPoint(self, tested_position, point):
    return sqrt((tested_position[0] - point[0]) ** 2 + (tested_position[1] - point[1]) ** 2)
  
  def positionIsNearPoint(self, tested_position, point):
    if self.getDistanceFromPoint(tested_position, point) <= self.width:
      return True
    return False
