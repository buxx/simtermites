from lib.brain.bug.termite.Termite import Termite
from config.Configuration import Configuration

class Queen(Termite):
  
  def __init__(self, host):
    Termite.__init__(self, host)
    self.move_wait_probability = Configuration.TERMITE_QUEEN_MOVE_WAIT_PROBABILITY