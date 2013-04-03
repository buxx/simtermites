from lib.brain.Brain import Brain
from lib.actions.Idle import Idle

class Object(Brain):
  
   def think(self, simulation):
    self.action = Idle(simulation, self)
  