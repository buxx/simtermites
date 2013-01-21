from lib.entity.bug.termite.Termite import Termite
from lib.brain.bug.termite.Larva import Larva as LarvaBrain
from collections import deque

class Larva(Termite):

  color = 255, 255, 255
  
  def __init__(self):
    Termite.__init__(self, LarvaBrain(self), 1)

  def getPosition(self):
    if self.carried_by == None:
      return self.position
    else:
      print('deplacement larve porte')
      return self.carried_by.getPosition()

  def setCarriedBy(self, carrier):
    self.carried_by = carrier
    self.trace = deque()

  def setCarriedByNone(self, host_putter):
    # etrange ... il n'y a rien dans self.carried_by, on utilise alors un parametre
    self.initializePosition(host_putter.getPosition())
    self.carried_by = None