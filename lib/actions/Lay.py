from lib.actions.Action import Action
from lib.entity.bug.termite.Larva import Larva

class Lay(Action):
  
  egg = None
  
  def __init__(self, simulation, brain):
    Action.__init__(self, simulation, brain)
    # TODO: le work (nursing la) devra etre dynamique
    self.egg  = Larva('Worker', 'Nursing')
  
  def do(self):
    if self.simulation.restriction.canDoAction('Lay_Worker_Nursing', \
    self.simulation.core.statistics.getData('Worker_Nursing', False, True) + self.simulation.core.statistics.getData('Larva_willbe_Worker_Nursing', True, True)):
      
      self.simulation.termites_simulator.addNewObjectToSimulation(self.brain.host.getLayPosition(), self.egg, False)
      self.simulation.core.statistics.increaseData('Larva_willbe_'+self.egg.getWillBeName())
