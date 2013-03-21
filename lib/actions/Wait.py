class Wait(object):
  
  brain = None
  direction = None
  
  def __init__(self, brain):
    self.brain = brain
    
  def do(self, termite_simulation):
    termite_simulation.simulation.mover.move(self.brain.host, self)