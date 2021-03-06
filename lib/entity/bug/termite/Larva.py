from lib.entity.bug.termite.Termite import Termite
from lib.brain.bug.termite.Larva import Larva as LarvaBrain
from collections import deque
from lib.entity.bug.termite.Worker import Worker
from config.Configuration import Configuration

class Larva(Termite):

  color = 255, 0, 0
  hatch_cyles = Configuration.LARVA_HATCH_CYCLES
  
  # TODO: PRendre en compte le type
  hatch_object = None
  
  def __init__(self, hatch_object):
    Termite.__init__(self, LarvaBrain(self), 1)
    self.hatch_object = hatch_object
  
  def getPosition(self):
    if self.carried_by == None:
      return self.position
    else:
      return self.carried_by.getPosition()
  
  def setCarriedBy(self, carrier):
    self.carried_by = carrier
    self.trace = deque()
  
  def runLifeCycle(self, simulation):
    Termite.runLifeCycle(self, simulation)
    #if self.carried_by == None:
    self.hatch_cyles = self.hatch_cyles - 1
    self.hatchIfReady(simulation)
  
  def hatchIfReady(self, simulation):
    if self.hatch_cyles == 0:
      # L'objet cree doit etre de classe dynamique
      worker_work = simulation.work_composer.getWorkForNewWorker()
      simulation.termites_simulator.addNewObjectToSimulation(self.getPosition(), Worker(worker_work))
      self.destroy(simulation)
  
  def destroy(self, simulation):
    if self.carried_by != None:
      self.carried_by.object_carried = None
      self.carried_by = None
    simulation.termites_simulator.deleteObjectFromSimulation(self)
  
  def puttedNearLarva(self):
    self.hatch_cyles = self.hatch_cyles - Configuration.LARVA_PUTTED_NEAR_LARVA_HATCH_BONUS
    if self.hatch_cyles < 1:
      self.hatch_cyles = 1
