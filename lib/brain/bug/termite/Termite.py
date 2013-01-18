from lib.brain.bug.Bug import Bug
from lib.actions.Move.Termite import Termite as TermiteMove
from config.Configuration import Configuration

class Termite(Bug):
  
  
  def __init__(self, host):
    Bug.__init__(self, host)
    self.move_wait_probability = Configuration.TERMITE_MOVE_WAIT_PROBABILITY
  
  def getMoveObject(self):
    return TermiteMove(self)