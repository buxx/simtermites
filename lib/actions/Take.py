from lib.actions.Action import Action
class Take(Action):

  good = None
  host = None

  def __init__(self, simulation, brain, host, good):
    Action.__init__(self, simulation, brain)
    self.host = host
    self.good = good

  def do(self):
    self.host.object_carried = self.good
    self.good.setCarriedBy(self.host)
    # TODO: La couleur ici c'est pas classe
    self.simulation.core.pygame.colorizer.colorizePixel(self.good.getPosition(), (0, 0, 0))
