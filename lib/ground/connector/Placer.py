from config.Configuration import Configuration

class Placer(object):
  """"""
  simulation = None
  
  def __init__(self, simulation):
    self.simulation = simulation
  
  def place(self, position, object_to_place):
    self.simulation.core.pygame.colorizer.colorizePixel(position, object_to_place.color)
    self.simulation.termites_simulator.termites.append(object_to_place)
    