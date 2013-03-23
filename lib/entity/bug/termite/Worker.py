from lib.entity.bug.termite.Termite import Termite
from lib.brain.bug.termite.Worker import Worker as WorkerBrain

class Worker(Termite):
  
  object_carried = None
  
  def getWorkerNameIfHaveWork(self):
    if self.brain.work != None:
      return self.__class__.__name__+'_'+self.brain.work
    return None
  
  def __init__(self, work = None):
    brain = WorkerBrain(self, work)
    Termite.__init__(self, brain, 2)
  
  def destroy(self, simulation):
    if self.object_carried != None:
      self.object_carried.setCarriedByNone(self)
    Termite.destroy(self, simulation)