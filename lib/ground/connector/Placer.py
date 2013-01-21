from config.Configuration import Configuration

class Placer(object):
  """"""
  screen = None
  simulation = None
  
  # TODO: screen doit etre encapsule (faire aussi pour Mover)
  def __init__(self, screen, simulation):
    self.screen = screen
    self.simulation = simulation
  
  def place(self, position, object_to_place):
    self.colorizePixel(position, object_to_place.color)
    self.simulation.termites_simulator.termites.append(object_to_place)
    
  def colorizePixel(self, position, color):
    self.screen.set_at(position, color)