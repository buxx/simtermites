from lib.entity.bug.termite.Termite import Termite

class King(Termite):
  
  def __init__(self, pos):
    Termite.__init__(self, pos, 2)