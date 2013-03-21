from lib.entity.bug.termite.Termite import Termite
from lib.brain.bug.termite.Queen import Queen as QueenBrain

class Queen(Termite):

  color = 255, 198, 35
  
  def __init__(self):
    brain = QueenBrain(self)
    Termite.__init__(self, brain, 6)
    
  def getLayPosition(self):
    position_last = self.getLastPosition()
    position_before_last = self.getBeforeLastPosition()
    position_last_x = position_last[0]
    position_last_y = position_last[1]
    position_before_last_x = position_before_last[0]
    position_before_last_y = position_before_last[1]
    
    if position_last_x -1 == position_before_last_x and position_last_y-1 == position_before_last_y:
      return (position_last_x+1, position_last_y+1)
    
    if position_last_x == position_before_last_x and position_last_y-1 == position_before_last_y:
      return (position_last_x, position_last_y+1)
    
    if position_last_x -1 == position_before_last_x and position_last_y+1 == position_before_last_y:
      return (position_last_x+1, position_last_y-1)
    
    if position_last_x  == position_before_last_x and position_last_y+1 == position_before_last_y:
      return (position_last_x, position_last_y-1)
    
    if position_last_x +1 == position_before_last_x and position_last_y == position_before_last_y:
      return (position_last_x-1, position_last_y)
    
    if position_last_x +1 == position_before_last_x and position_last_y-1 == position_before_last_y:
      return (position_last_x-1, position_last_y+1)
    
    if position_last_x == position_before_last_x and position_last_y-1 == position_before_last_y:
      return (position_last_x, position_last_y+1)
    
    if position_last_x-1 == position_before_last_x and position_last_y == position_before_last_y:
      return (position_last_x+1, position_last_y)
    
    if position_last_x == position_before_last_x and position_last_y == position_before_last_y:
      return (position_last_x, position_last_y)
    
    if position_last_x+1 == position_before_last_x and position_last_y+1 == position_before_last_y:
      return (position_last_x-1, position_last_y-1)
    
    print("Unable to find last position for lay position")
    return (position_last_x, position_last_y)