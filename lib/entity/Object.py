from collections import deque

class Object(object):
  
  color = 255, 255, 255
  position = None
  carried_by = None
  brain = None
  trace = None
  
  def __init__(self, brain):
    self.brain = brain
    self.trace = deque()
  
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
    
  def setCarriedBy(self, carrier):
    self.carried_by = carrier
  
  def setCarriedByNone(self, host_putter):
    # etrange ... il n'y a rien dans self.carried_by, on utilise alors un parametre
    self.initializePosition(host_putter.getPosition())
    self.carried_by = None
    
  def initializePosition(self, position):
    self.setPosition(position)
    self.trace.appendleft(position)
  
  def runLifeCycle(self, simulation):
    pass
    
  def think(self, simulation):
    self.brain.think(simulation)
    
  def doAction(self):
    self.brain.action.do()
