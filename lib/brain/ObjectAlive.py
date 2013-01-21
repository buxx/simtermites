from lib.brain.Brain import Brain
import random

class ObjectAlive(Brain):
  
  """
    move_probability n'est pas la probabilite que l'action soit de se deplacer
    mais la probabilite qu'elle effectue son deplacement si l'action doit etre
    move
  """
  move_wait_probability = None
  action = None
  
  def __init__(self, host):
    Brain.__init__(self, host)
    
  def think(self, simulation):
    action = self.getAction(simulation)
    if not action:
      if (self.moveButTakeWait()):
        self.action = self.getWaitObject();
      else:
        self.action = self.getMoveObject();
    else:
      self.action = action
    
  def getMoveObject(self):
    raise Exception("Cette methode doit etre implemente par un objet enfant")
    
  def getWaitObject(self):
    raise Exception("Cette methode doit etre implemente par un objet enfant")
  
  def getAction(self, simulation):
    raise Exception("Cette methode doit etre implemente par un objet enfant")
  
  def moveButTakeWait(self):
    randomint = random.randint(1, self.move_wait_probability[1])
    if (randomint >= 1 and randomint <= self.move_wait_probability[0]):
      return True
    return False
  