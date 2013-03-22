from lib.actions.Action import Action
import random
from config.Configuration import Configuration

class Move(Action):
  
  direction = None
  new_coordonates = None
  brain = None
  
  direction_same_way_probability = None
  same_way_slightly_turn_probability = None
  
  def __init__(self, simulation, brain):
    Action.__init__(self, simulation, brain)
    self.determineDirection()
  
  def do(self):
    self.simulation.mover.move(self.brain.host, self)
  
  def determineDirection(self):
    self.getNewDirection()
    nursery = self.simulation.getZoneIfExist('Nursery')
    if nursery != None:
      if not nursery.positionIsInArea(self.new_coordonates):
        self.direction_same_way_probability = [0,100]
        self.determineDirection()
  
  def getNewDirection(self):
    if self.takeSameDirection():
      if self.isSlightlyTurn():
        self.direction = self.getSlightlyTurn(self.brain.host.last_direction)
        self.brain.host.last_direction = self.direction
      else:
        self.direction = self.brain.host.last_direction
    else:
      self.direction = random.randint(0, 7)
      self.brain.host.last_direction = self.direction
    self.new_coordonates = self.movePixel(self.brain.host.getPosition(), self.direction)
  
  def takeSameDirection(self):
    randomint = random.randint(1, self.direction_same_way_probability[1])
    if randomint >= 1 and randomint <= self.direction_same_way_probability[0] \
       and self.brain.host.last_direction != None :
      return True
    return False
  
  def isSlightlyTurn(self):
    randomint = random.randint(1, self.same_way_slightly_turn_probability[1])
    if randomint >= 1 and randomint <= self.same_way_slightly_turn_probability[0]:
      return True
    return False
  
  def getSlightlyTurn(self, last_direction):
    randomint = random.randint(last_direction-1, last_direction+1)
    if randomint == -1:
      randomint = 7
    if randomint == 8:
      randomint = 0
    return randomint
  
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
      return (Configuration.CONF_SCREEN_WIDTH_MIDDLE, Configuration.CONF_SCREEN_HEIGHT_MIDDLE)
    else:
      return (int(x), int(y))
