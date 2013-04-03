from lib.actions.Action import Action
class Idle(Action):
  
  brain = None
  direction = None
  
  def __init__(self, simulation, brain):
    Action.__init__(self, simulation, brain)
    
  def do(self):
    self.simulation.mover.move(self.brain.host, self)