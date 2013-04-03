from lib.simulation.zone.Nursery import Nursery
from lib.simulation.zone.PlantFood import PlantFood
from lib.simulation.zone.PlantRepository import PlantRepository
from config.Configuration import Configuration

class TermitesSimulator(object):
  
  simulation = None
  termites = []
  
  def __init__(self, simulation, termites):
    self.simulation = simulation
    self.termites = termites
    self.simulation.addZone(Nursery((Configuration.ZONE_NURSERY_POSITION[0], Configuration.ZONE_NURSERY_POSITION[1]), Configuration.ZONE_NURSERY_RADIUS))
    self.simulation.addZone(PlantFood((Configuration.ZONE_NURSERY_POSITION[0], 0),120))
    self.simulation.addZone(PlantRepository((Configuration.ZONE_NURSERY_POSITION[0]/2, Configuration.ZONE_NURSERY_POSITION[1]),125))
    
  def runActions(self):
    
    for termite in self.termites:
      # TODO: Nettoyer ca
      existInDeletedList = False
      try:
        existInDeletedList = self.simulation.just_deleted_objects.index(termite)
      except:
        pass
      
      if not existInDeletedList:
        
        termite.think(self.simulation)
        termite.doAction()
        if self.simulation.lifecycle_now:
          termite.runLifeCycle(self.simulation)
        self.simulation.addObjectPositionInGrid(termite)
    
  def addNewObjectToSimulation(self, position, object, increase_statistics_data = True):
    self.simulation.addNewObjectToSimulation(position, object, increase_statistics_data)
  
  def deleteObjectFromSimulation(self, object):
    self.termites[:] = [p for p in self.termites if p != object]
    self.simulation.deleteObjectFromSimulation(object)
