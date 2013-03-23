from lib.brain.bug.termite.Termite import Termite
from lib.actions.Take import Take
from lib.actions.PutLarva import PutLarva

class Worker(Termite):

  def __init__(self, host, work = None):
    Termite.__init__(self, host)
    self.work = work
  
  def getAction(self, simulation):
    if self.work == 'Nursing':
      # TODO: il faudra passer un tableau de types d'objet
      # pour ne faire cette demande qu'une seule fois
      larva_near = simulation.findObjectNearPosition('Larva', self.host.getPosition(), 1, False)
      #larva_near = None
      if larva_near != None:
        if self.host.object_carried == None:
          return Take(simulation, self, self.host, larva_near)
        elif self.host.object_carried.__class__.__name__ == 'Larva':
          return PutLarva(simulation, self, self.host, self.host.object_carried)
    return None