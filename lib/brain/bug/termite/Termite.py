from lib.brain.bug.Bug import Bug
from lib.actions.Move.Termite import Termite as TermiteMove
from config.Configuration import Configuration
from lib.actions.Wait import Wait

class Termite(Bug):
  
  
  def __init__(self, host):
    Bug.__init__(self, host)
    self.move_wait_probability = Configuration.TERMITE_MOVE_WAIT_PROBABILITY
  
  def getMoveObject(self, simulation):
    return TermiteMove(simulation, self)
  
  def getWaitObject(self, simulation):
    return Wait(simulation, self)