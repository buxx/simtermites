from lib.tool.Probability import Probability

class Composer(object):
  
  simulation = None
  
  def __init__(self, simulation):
    self.simulation = simulation
  
  def getWorkForNewWorker(self):
    
    choices_percents = [
      self.simulation.core.configuration.WORKER_ORDER_NURSING,
      self.simulation.core.configuration.WORKER_ORDER_FOODING
    ]
    choices_actions_correspondance = [
      'Nursing',
      'Fooding'
    ]
    
    if not self.simulation.restriction.canDoAction('Lay_Worker_Nursing', self.simulation.core.statistics.getData('Worker_Nursing', False, True)):
      del choices_percents[0]
      del choices_actions_correspondance[0]
    
    return choices_actions_correspondance[Probability.getChoiceForPercents(choices_percents)]