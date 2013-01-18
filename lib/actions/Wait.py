class Wait(object):
  
  brain = None
  direction = None
  
  def __init__(self, brain):
    self.brain = brain
    
  def do(self, simulation):
    simulation.mover.move(self.brain.host, self)