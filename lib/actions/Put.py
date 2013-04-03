from lib.actions.Action import Action
class Put(Action):

  good = None
  host = None

  def __init__(self, simulation, brain, host, good):
    Action.__init__(self, simulation, brain)
    self.host = host
    self.good = good

  def do(self):
    self.good.setCarriedByNone(self.host)
    self.host.object_carried = None
    self.simulation.core.pygame.colorizer.colorizePixel(self.good.position, self.good.color)
    # on dit a la termite de ne pas prendre de larve pendant un moment
    # TODO: Il faudrait que ce soit plus propre et interdire une action (comme Take)
    self.host.brain.addForcedAction('Move', 25)
