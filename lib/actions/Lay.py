from lib.actions.Action import Action
from lib.entity.bug.termite.Larva import Larva

class Lay(Action):
  
  egg = None
  
  def __init__(self, simulation, brain):
    Action.__init__(self, simulation, brain)
    # TODO: le work (nursing la) devra etre dynamique
    self.egg  = Larva('Nursing')
  
  def do(self):
    if self.simulation.restriction.canDoAction('Lay', 'Worker_Nursing'):
      self.simulation.termites_simulator.addNewObjectToSimulation(self.brain.host.getLayPosition(), self.egg)
