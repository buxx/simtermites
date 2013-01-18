from lib.entity.Object import Object
from collections import deque

class ObjectAlive(Object):
  
  trace = None
  last_direction = None
  length = None
  brain = None
  
  def __init__(self, brain, pos, length):
    
    Object.__init__(self)
    
    self.brain = brain
    self.trace = deque()
    self.length = length
    
    i = 1
    while i <= self.length:
      self.trace.appendleft(pos)
      i = i+1
      
  def updateTrace(self, pos):
    self.trace.appendleft(pos)
    del self.trace[self.length]
  
  def think(self):
    self.brain.think()