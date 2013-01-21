class Take(object):

  good = None
  host = None

  def __init__(self, host, good):
    self.host = host
    self.good = good

  def do(self, simulation):
    self.host.object_carried = self.good
    self.good.setCarriedBy(self.host)
    # TODO: La couleur ici c'est pas classe
    simulation.core.pygame.colorizer.colorizePixel(self.good.position, (0, 0, 0))