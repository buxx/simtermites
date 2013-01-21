from lib.entity.bug.termite.Larva import Larva

class Lay(object):
  
  egg = None
  
  def __init__(self, brain):
    self.brain = brain
    # TODO: La position doit etre mise dans les objectalive par le Placer
    self.egg  = Larva((320, 240))
  
  def do(self, simulation):
    simulation.placer.place(self.brain.host.getLayPosition(), self.egg)
  