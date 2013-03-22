from lib.actions.Action import Action
from lib.entity.bug.termite.Larva import Larva

class Lay(Action):
  
  egg = None
  
  def __init__(self, simulation, brain):
    Action.__init__(self, simulation, brain)
    self.egg  = Larva()
  
  def do(self):
    self.simulation.termites_simulator.addNewObjectToSimulation(self.brain.host.getLayPosition(), self.egg)
  