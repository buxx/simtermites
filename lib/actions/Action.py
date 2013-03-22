class Action(object):
  
  simulation = None
  brain = None
  
  def __init__(self, simulation, brain):
    self.simulation = simulation
    self.brain = brain