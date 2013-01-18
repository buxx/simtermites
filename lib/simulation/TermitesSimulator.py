class TermitesSimulator(object):
  
  simulation = None
  termites = []
  
  def __init__(self, simulation, termites):
    self.simulation = simulation
    self.termites = termites
  
  def runActions(self):
    for termite in self.termites:
      termite.think()
      termite.brain.action.do(self.simulation)