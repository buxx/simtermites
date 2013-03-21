from lib.entity.bug.termite.Larva import Larva

class Lay(object):
  
  egg = None
  
  def __init__(self, brain):
    self.brain = brain
    self.egg  = Larva()
  
  def do(self, termite_simulation):
    termite_simulation.addNewObjectToSimulation(self.brain.host.getLayPosition(), self.egg)
  