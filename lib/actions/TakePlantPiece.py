from lib.actions.Take import Take
from lib.entity.PlantPiece import PlantPiece

class TakePlantPiece(Take):
  
  def __init__(self, simulation, brain, host):
    plant_piece = PlantPiece()
    Take.__init__(self, simulation, brain, host, plant_piece)
    simulation.termites_simulator.addNewObjectToSimulation(self.host.getPosition(), plant_piece)
