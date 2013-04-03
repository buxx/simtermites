class Placer(object):
  """"""
  simulation = None
  
  def __init__(self, simulation):
    self.simulation = simulation
  
  def place(self, position, object_to_place):
    object_to_place.initializePosition(position)
    self.simulation.core.pygame.colorizer.colorizePixel(position, object_to_place.color)
    # TODO: il faut deplacer ca vers le core ou le simulator
    self.simulation.termites_simulator.termites.append(object_to_place)
    