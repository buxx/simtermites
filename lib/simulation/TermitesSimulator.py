from lib.simulation.zone.Nursery import Nursery
from config.Configuration import Configuration

class TermitesSimulator(object):
  
  simulation = None
  termites = []
  
  def __init__(self, simulation, termites):
    self.simulation = simulation
    self.termites = termites
    self.simulation.addZone(Nursery((Configuration.CONF_SCREEN_WIDTH_MIDDLE, Configuration.CONF_SCREEN_HEIGHT_MIDDLE),100))
  
  def runActions(self):
    for termite in self.termites:
      termite.think(self.simulation)
      termite.doAction()
      self.simulation.addObjectPositionInGrid(termite)
  
  def addNewObjectToSimulation(self, position, object):
    self.termites.append(object)
    self.simulation.addNewObjectToSimulation(position, object)