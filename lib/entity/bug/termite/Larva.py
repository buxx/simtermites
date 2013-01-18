from lib.entity.bug.termite.Termite import Termite

class Larva(Termite):
  
  def __init__(self, pos):
    Termite.__init__(self, pos, 1)