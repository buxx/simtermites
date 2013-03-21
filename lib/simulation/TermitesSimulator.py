class TermitesSimulator(object):
  
  simulation = None
  termites = []
  
  def __init__(self, simulation, termites):
    self.simulation = simulation
    self.termites = termites
  
  def runActions(self):
    for termite in self.termites:
      termite.think(self.simulation)
      termite.doAction(self)
      self.simulation.addObjectPositionInGrid(termite)
  
  def addNewObjectToSimulation(self, position, object):
    self.termites.append(object)
    self.simulation.addNewObjectToSimulation(position, object)