from lib.brain.bug.termite.Termite import Termite
from config.Configuration import Configuration
from lib.actions.Lay import Lay

class Queen(Termite):
  
  cycles_since_lay = 0
  
  def __init__(self, host):
    Termite.__init__(self, host)
    self.move_wait_probability = Configuration.TERMITE_QUEEN_MOVE_WAIT_PROBABILITY
    
  def getAction(self):
    if self.cycles_since_lay < Configuration.TERMITE_QUEEN_LAY_EACH_CYCLE:
      self.cycles_since_lay = self.cycles_since_lay+1
    else:
      self.cycles_since_lay = 0
      return Lay(self)