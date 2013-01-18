from lib.entity.bug.termite.Termite import Termite
from lib.brain.bug.termite.Queen import Queen as QueenBrain

class Queen(Termite):
  
  color = 255, 0, 0
  
  def __init__(self, pos):
    brain = QueenBrain(self)
    Termite.__init__(self, brain, pos, 6)