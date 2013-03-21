class Put(object):

  good = None
  host = None

  def __init__(self, host, good):
    self.host = host
    self.good = good

  def do(self, termite_simulation):
    self.good.setCarriedByNone(self.host)
    self.host.object_carried = None
    termite_simulation.simulation.core.pygame.colorizer.colorizePixel(self.good.position, self.good.color)
    # on dit a la termite de ne pas prendre de larve pendant un moment
    self.host.brain.addForcedAction('Move', 55)