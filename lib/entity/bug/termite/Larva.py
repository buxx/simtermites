from lib.entity.bug.termite.Termite import Termite
from lib.brain.bug.termite.Larva import Larva as LarvaBrain
from collections import deque
from lib.entity.bug.termite.Worker import Worker
from config.Configuration import Configuration

class Larva(Termite):

  color = 255, 0, 0
  hatch_cyles = Configuration.LARVA_HATCH_CYCLES
  
  def __init__(self):
    Termite.__init__(self, LarvaBrain(self), 1)

  def getPosition(self):
    if self.carried_by == None:
      return self.position
    else:
      return self.carried_by.getPosition()

  def setCarriedBy(self, carrier):
    self.carried_by = carrier
    self.trace = deque()

  def setCarriedByNone(self, host_putter):
    # etrange ... il n'y a rien dans self.carried_by, on utilise alors un parametre
    self.initializePosition(host_putter.getPosition())
    self.carried_by = None
  
  def runLifeCycle(self, simulation):
    Termite.runLifeCycle(self, simulation)
    if self.carried_by == None:
      self.hatch_cyles = self.hatch_cyles - 1
      self.hatchIfReady(simulation)
  
  def hatchIfReady(self, simulation):
    if self.hatch_cyles == 0:
      simulation.termites_simulator.addNewObjectToSimulation(self.getPosition(), Worker('Nursing'))
      self.destroy(simulation)
  
  def destroy(self, simulation):
    if self.carried_by != None:
      self.carried_by.object_carried = None
    simulation.termites_simulator.deleteObjectFromSimulation(self)
