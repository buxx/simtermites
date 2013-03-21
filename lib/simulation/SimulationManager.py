from config.Configuration import Configuration
from lib.simulation.TermitesSimulator import TermitesSimulator
from lib.ground.connector.Mover import Mover
from lib.ground.connector.Placer import Placer
from lib.entity.bug.termite.Worker import Worker as TermiteWorker
from lib.entity.bug.termite.Queen import Queen as TermiteQueen
from lib.tool.Position import get_near_coordonates_for_position

class SimulationManager(object):
  
  core = None
  termites_simulator = None
  mover = None
  placer = None
  
  objects_positions_grid = {}
  objects_positions_grid_previous_cycle = {}
  
  def __init__(self, Core):
    self.core = Core
    self.mover = Mover(self)
    self.placer = Placer(self)
    self.initializeBugs()
  
  def initializeBugs(self):
    self.termites_simulator = TermitesSimulator(self, [])
    termites_count = 1
    while termites_count <= Configuration.CONF_TERMITES_COUNT:
      self.placer.place((Configuration.CONF_SCREEN_WIDTH_MIDDLE, Configuration.CONF_SCREEN_HEIGHT_MIDDLE), TermiteWorker())
      termites_count = termites_count+1
    self.placer.place((Configuration.CONF_SCREEN_WIDTH_MIDDLE, Configuration.CONF_SCREEN_HEIGHT_MIDDLE), TermiteQueen())
  
  def runCycle(self):
    # On clean les coordonees
    self.objects_positions_grid_previous_cycle = self.objects_positions_grid
    self.objects_positions_grid = {}
    
    self.termites_simulator.runActions()
    self.core.updateDisplay()
    if (Configuration.CONF_CLOCK_TICK):
      self.core.pygame.clock.tick(Configuration.CONF_CLOCK_TICK)
  
  def addObjectPositionInGrid(self, object):
    
    if object.carried_by == None:
      position_key = str(object.getPosition()[0])+'.'+str(object.getPosition()[1])
      if position_key in self.objects_positions_grid:
        self.objects_positions_grid[position_key].append(object)
      else:
        self.objects_positions_grid[position_key] = [object]
    
    
  def addNewObjectToSimulation(self, position, object):
    self.placer.place(position, object)

  def findObjectNearPosition(self, object_class, position_ref, distance, allow_same_position):
    possibles_coordonates = get_near_coordonates_for_position(position_ref, distance, allow_same_position)
    
    for coordonate in possibles_coordonates:
      coordonate_key = str(coordonate[0])+'.'+str(coordonate[1])
      if coordonate_key in self.objects_positions_grid_previous_cycle:
        for object in self.objects_positions_grid_previous_cycle[coordonate_key]:
          if object.__class__.__name__ == object_class:
            return object

  def getObjects(self):
    # TODO: Il y a peut-etre confusion: on met actuellement les
    # objets termites dans TermiteSimulator. Or il faudrai que les
    # objets soit dans SimulationManager et que TermiteSimulator pioche
    # les objets termites dans les objets de la simulation
    return self.termites_simulator.termites