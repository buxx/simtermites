from lib.entity.bug.termite.Termite import Termite
from lib.brain.bug.termite.Worker import Worker as WorkerBrain

class Worker(Termite):
  
  object_carried = None
  
  def __init__(self):
    brain = WorkerBrain(self)
    Termite.__init__(self, brain, 2)