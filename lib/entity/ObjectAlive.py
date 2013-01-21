from lib.entity.Object import Object
from collections import deque

class ObjectAlive(Object):
  
  trace = None
  last_direction = None
  length = None
  brain = None
  
  def __init__(self, brain, length):
    
    Object.__init__(self)
    
    self.brain = brain
    self.trace = deque()
    self.length = length
   
  def initializePosition(self, position):
    self.setPosition(position, False)
    i = 1
    while i <= self.length:
      self.trace.appendleft(position)
      i = i+1

  def setPosition(self, position, update_trace = True):
    super(ObjectAlive, self).setPosition(position)
    if (update_trace):
      self.updateTrace(position)
    
  def updateTrace(self, pos):
    self.trace.appendleft(pos)
    del self.trace[self.length]
  
  def think(self, simulation):
    self.brain.think(simulation)
    
  def doAction(self, simulation):
    self.brain.action.do(simulation)

  def getPosition(self):
    return self.trace[0]

  def getLastPosition(self):
    return self.trace[self.length-1]
    
  def getBeforeLastPosition(self):
    return self.trace[self.length-2]