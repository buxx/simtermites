from lib.entity.bug.termite.Termite import Termite
from lib.brain.bug.termite.Worker import Worker as WorkerBrain

class Worker(Termite):
  
  def __init__(self, pos):
    brain = WorkerBrain(self)
    Termite.__init__(self, brain, pos, 2)