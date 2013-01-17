from lib.entity.Object import Object
from collections import deque

class ObjectAlive(Object):
  
  trace = None
  length = None
  
  def __init__(self, pos, length):
    
    Object.__init__(self)
    
    # On itinialise la trace
    self.trace = deque()
    self.length = length
    
    i = 1
    while i <= self.length:
      self.trace.appendleft(pos)
      i = i+1
      
  def updateTrace(self, pos):
    self.trace.appendleft(pos)
    del self.trace[self.length]