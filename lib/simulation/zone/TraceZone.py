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
      if sqrt((tested_position[0] - coordonate[0]) ** 2 + (tested_position[1] - coordonate[1]) ** 2) < self.width:
        return True
    return False
