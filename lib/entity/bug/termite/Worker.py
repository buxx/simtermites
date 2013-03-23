from lib.entity.bug.termite.Termite import Termite
from lib.brain.bug.termite.Worker import Worker as WorkerBrain
from config.Configuration import Configuration

class Worker(Termite):
  
  object_carried = None
  
  def __init__(self, work = None):
    brain = WorkerBrain(self, work)
    Termite.__init__(self, brain, 2)
    self.lifecycle_left = Configuration.TERMITES_LIFETIMES['Worker']
  
  def destroy(self, simulation):
    if self.object_carried != None:
      self.object_carried.setCarriedByNone(self)
    Termite.destroy(self, simulation)