class Object(object):
  
  color = 255, 255, 255
  position = None
  carried_by = None
  
  def getId(self):
    return self.__class__.__name__
  
  def setPosition(self, position):
    self.position = position
  
  def getPosition(self):
    return self.position
  
  # TODO: Ce code est dans tool.Position maintenant
  def isNear(self, position_to_compare, distance):
    position_x = self.position[0]
    position_y = self.position[1]
    position_to_compare_x = position_to_compare[0]
    position_to_compare_y = position_to_compare[1]

    if (position_to_compare_x == position_x or \
    position_to_compare_x == position_x-distance or \
    position_to_compare_x == position_x+distance) and \
    (position_to_compare_y == position_y or \
    position_to_compare_y == position_y-distance or \
    position_to_compare_y == position_y+distance):
      return True