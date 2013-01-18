import random

class Move(object):
  
  direction = None
  brain = None
  
  direction_same_way_probability = None
  same_way_slightly_turn_probability = None
  
  def __init__(self, brain):
    self.brain = brain
    self.determineDirection()
  
  def do(self, simulation):
    simulation.mover.move(self.brain.host, self)
  
  def determineDirection(self):
    
    if self.takeSameDirection():
      if self.isSlightlyTurn():
        self.direction = self.getSlightlyTurn(self.brain.host.last_direction)
        self.brain.host.last_direction = self.direction
      else:
        self.direction = self.brain.host.last_direction
    else:
      self.direction = random.randint(0, 7)
      self.brain.host.last_direction = self.direction
  
  
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