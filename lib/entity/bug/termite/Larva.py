from lib.entity.bug.termite.Termite import Termite
from lib.brain.bug.termite.Larva import Larva as LarvaBrain

class Larva(Termite):
  
  color = 255, 255, 255
  
  def __init__(self, pos):
    Termite.__init__(self, LarvaBrain(self), pos, 1)