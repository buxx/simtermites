from lib.brain.bug.termite.Termite import Termite
from lib.actions.Wait import Wait

class Larva(Termite):
  
  def __init__(self, host):
    Termite.__init__(self, host)
  
  def getAction(self):
    return Wait(self)