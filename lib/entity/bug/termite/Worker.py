from lib.entity.bug.termite.Termite import Termite
from lib.brain.bug.termite.Worker import Worker as WorkerBrain

class Worker(Termite):
  
  object_carried = None
  debug_caried_cycles = 25
  
  def getId(self):
    if self.brain.work != None:
      return self.__class__.__name__+'_'+self.brain.work
    return Termite.getId(self)
  
  def __init__(self, work = None):
    brain = WorkerBrain(self, work)
    Termite.__init__(self, brain, 2)
  
  def destroy(self, simulation):
    if self.object_carried != None:
      self.object_carried.setCarriedByNone(self)
    Termite.destroy(self, simulation)
  
  def think(self, simulation):
    self.debugCarriedObject()
    Termite.think(self, simulation)
  
  def debugCarriedObject(self):
    if self.object_carried != None:
      self.debug_caried_cycles = self.debug_caried_cycles -1
      if self.debug_caried_cycles == 0:
        self.debug_caried_cycles = 25
        try:
          simulation.termites_simulator.termites.index(self.object_carried)
        except:
          self.object_carried.carried_by = None
          self.object_carried = None
        