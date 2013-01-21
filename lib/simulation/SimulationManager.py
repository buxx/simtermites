from config.Configuration import Configuration
from lib.simulation.TermitesSimulator import TermitesSimulator
from lib.ground.connector.Mover import Mover
from lib.ground.connector.Placer import Placer
from lib.entity.bug.termite.Worker import Worker as TermiteWorker
from lib.entity.bug.termite.Queen import Queen as TermiteQueen
from lib.tool.Position import positions_near

class SimulationManager(object):
  
  core = None
  termites_simulator = None
  mover = None
  placer = None
  objects_positions_index = []
  
  def __init__(self, Core):
    self.core = Core
    self.mover = Mover(self)
    self.placer = Placer(self)
    self.initializeBugs()
  
  def initializeBugs(self):
    self.termites_simulator = TermitesSimulator(self, [])
    termites_count = 1
    while termites_count <= Configuration.CONF_TERMITES_COUNT:
      self.placer.place((320, 240), TermiteWorker())
      termites_count = termites_count+1
    self.placer.place((320, 240), TermiteQueen())
  
  def runCycle(self):
    self.termites_simulator.runActions()
    self.core.updateDisplay()
    self.updateObjectsPositionsIndex()
    if (Configuration.CONF_CLOCK_TICK):
      self.core.pygame.clock.tick(Configuration.CONF_CLOCK_TICK)

  def updateObjectsPositionsIndex(self):
    self.objects_positions_index = []
    for object in self.termites_simulator.termites:
      if object.carried_by == None:
        record = (object.position, object)
        self.objects_positions_index.append(record)

  # Mangeur de ressource ?
  def findObjectNearPosition(self, object_class, position_ref, distance, allow_same_position):
    # todo: optimisation : objects_positions_index avec tableaux possedant que certains types d'objets
    # pour parcourir moins d'elements
    for position in self.objects_positions_index:
      if position[1].__class__.__name__ == object_class:
        if positions_near(position_ref, position[0], distance, allow_same_position):
          return position[1]
    return None

  def getObjects(self):
    # TODO: Il y a peut-etre confusion: on met actuellement les
    # objets termites dans TermiteSimulator. Or il faudrai que les
    # objets soit dans SimulationManager et que TermiteSimulator pioche
    # les objets termites dans les objets de la simulation
    return self.termites_simulator.termites