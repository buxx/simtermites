from lib.entity.Object import Object
from lib.actions.Idle import Idle
from lib.brain.Object import Object as ObjectBrain

class PlantPiece(Object):
  
  color = 0, 187, 5
  
  def __init__(self):
    Object.__init__(self, ObjectBrain(self))
  
  def getPosition(self):
    if self.carried_by == None:
      return self.position
    else:
      return self.carried_by.getPosition()
  