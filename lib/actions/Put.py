class Put(object):

  good = None
  host = None

  def __init__(self, host, good):
    self.host = host
    self.good = good

  def do(self, simulation):
    self.good.setCarriedByNone(self.host)
    self.host.object_carried = None
    simulation.core.pygame.colorizer.colorizePixel(self.good.position, self.good.color)