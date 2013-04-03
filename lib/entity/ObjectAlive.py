from lib.entity.Object import Object
from config.Configuration import Configuration

class ObjectAlive(Object):
  
  last_direction = None
  length = None
  lifecycle_left = -1
  
  def __init__(self, brain, length):
    Object.__init__(self, brain)
    self.length = length
    
    if self.__class__.__name__ in Configuration.TERMITES_LIFETIMES:
      self.lifecycle_left = Configuration.TERMITES_LIFETIMES[self.__class__.__name__]
   
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
  
  def getPosition(self):
    return self.trace[0]
  
  def getLastPosition(self):
    return self.trace[self.length-1]
  
  def getBeforeLastPosition(self):
    return self.trace[self.length-2]
  
  def runLifeCycle(self, simulation):
    if self.lifecycle_left != None:
      self.lifecycle_left = self.lifecycle_left - 1
      self.destroyIfLifeCyclesFinished(simulation)
  
  def destroyIfLifeCyclesFinished(self, simulation):
    if self.lifecycle_left == 0:
      self.destroy(simulation)
  
  def destroy(self, simulation):
    simulation.termites_simulator.deleteObjectFromSimulation(self)
  
  def getWorkerNameIfHaveWork(self):
    return None
