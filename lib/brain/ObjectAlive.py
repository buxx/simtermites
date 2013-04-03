from lib.brain.Brain import Brain
import random

class ObjectAlive(Brain):
  
  """
    move_probability n'est pas la probabilite que l'action soit de se deplacer
    mais la probabilite qu'elle effectue son deplacement si l'action doit etre
    move
  """
  move_wait_probability = None
  action_forced_class = None
  action_forced_cycles = 0
  work = None
  
  def __init__(self, host):
    Brain.__init__(self, host)
    
  def think(self, simulation):
    action = self.getActionIfHaveForcedAction(simulation)
    if not action:
      action = self.getAction(simulation)
    if not action:
      if (self.moveButTakeWait()):
        self.action = self.getWaitObject(simulation);
      else:
        self.action = self.getMoveObject(simulation);
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
  
  def addForcedAction(self, forced_action_class, forced_cycles):
    self.action_forced_class = forced_action_class
    self.action_forced_cycles = forced_cycles
  
  def getActionIfHaveForcedAction(self, simulation):
    if self.action_forced_class:
      self.action_forced_cycles = self.action_forced_cycles-1
      if self.action_forced_cycles < 1:
        self.action_forced_class = None
      # TODO: Pour le moment c'est forced l objet action !
      return self.getMoveObject(simulation)
    return None
