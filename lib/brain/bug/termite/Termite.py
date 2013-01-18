from lib.brain.bug.Bug import Bug
from lib.actions.Bug.Termite import Termite as TermiteMove

class Termite(Bug):
  
  def __init__(self, host):
    Bug.__init__(self, host)
  
  def think(self):
    return TermiteMove(self)