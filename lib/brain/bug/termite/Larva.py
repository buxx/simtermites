from lib.brain.bug.termite.Termite import Termite
from lib.actions.Idle import Idle

class Larva(Termite):
  
  def __init__(self, host):
    Termite.__init__(self, host)
  
  def getAction(self, simulation):
    return Idle(simulation, self)