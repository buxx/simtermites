from config.Configuration import Configuration
from lib.simulation.TermitesSimulator import TermitesSimulator
from lib.ground.connector.Mover import Mover
from lib.ground.connector.Placer import Placer
from lib.entity.bug.termite.Worker import Worker as TermiteWorker
from lib.entity.bug.termite.Queen import Queen as TermiteQueen
from lib.tool.Position import get_near_coordonates_for_position
from lib.simulation.Restriction import Restriction
from lib.simulation.work.Composer import Composer
from collections import deque
from lib.entity.PlantPiece import PlantPiece

class SimulationManager(object):
  
  core = None
  termites_simulator = None
  mover = None
  placer = None
  zones = {}
  trace_zones = {}
  restriction = None
  work_composer = None
  
  # TODO: bien place le system de compteur de stats ?
  statistics_display_counter = 25
  filecycle_counter = Configuration.LILECYCLE_EACH_CYCLE
  lifecycle_now = False
  
  objects_positions_grid = {}
  objects_positions_grid_previous_cycle = {}
  
  def __init__(self, Core):
    self.core = Core
    self.mover = Mover(self)
    self.placer = Placer(self)
    self.restriction = Restriction(self)
    self.work_composer = Composer(self)
    self.initializeBugs()
  
  def initializeBugs(self):
    self.termites_simulator = TermitesSimulator(self, [])
    termites_count = 1
    while termites_count <= Configuration.CONF_TERMITES_COUNT_WORKER_NOWORK:
      self.placer.place((Configuration.CONF_SCREEN_WIDTH_MIDDLE, Configuration.CONF_SCREEN_HEIGHT_MIDDLE), TermiteWorker('Fooding'))
      termites_count = termites_count+1
      self.core.statistics.increaseData('Worker_Fooding')
    termites_count = 0
    while termites_count <= Configuration.CONF_TERMITES_COUNT_WORKER_NURSING:
      self.placer.place((Configuration.CONF_SCREEN_WIDTH_MIDDLE, Configuration.CONF_SCREEN_HEIGHT_MIDDLE), TermiteWorker('Nursing'))
      termites_count = termites_count+1
      self.core.statistics.increaseData('Worker_Nursing')
    self.placer.place((Configuration.CONF_SCREEN_WIDTH_MIDDLE, Configuration.CONF_SCREEN_HEIGHT_MIDDLE), TermiteQueen('Queening'))
    self.core.statistics.increaseData('Queen')
    
    # TODO: Pour le moment on doit placer au moin une PlantPiece pour que les termites worker Fooding
    # depose leur morceau de plante
    plant_piece = PlantPiece()
    plant_piece.initializePosition((Configuration.ZONE_NURSERY_POSITION[0]-50, Configuration.ZONE_NURSERY_POSITION[1]))
    self.addNewObjectToSimulation(plant_piece.getPosition(), plant_piece)
    #
  
  def runCycle(self):
    # On clean les coordonees
    self.objects_positions_grid_previous_cycle = self.objects_positions_grid
    self.objects_positions_grid = {}
    
    # hardcode pour test
    if self.core.ask_draw_roads == True:
      self.core.drawAllRoads()
      self.core.ask_draw_roads = False
    
    self.displayZones()
    self.termites_simulator.runActions()
    self.updateStatisticsIfCount()
    self.runLifeCyclecounter()
    self.core.updateDisplay()
    
    if (self.core.configuration.CONF_CLOCK_TICK):
      self.core.pygame.clock.tick(self.core.configuration.CONF_CLOCK_TICK)
  
  def displayZones(self):
    for zone_id in self.zones:
      if self.zones[zone_id].draw == True:
        self.core.pygame.draw_circle(self.zones[zone_id].color, self.zones[zone_id].position, self.zones[zone_id].radius, self.zones[zone_id].draw_width)
  
  def updateStatisticsIfCount(self):
    if self.statistics_display_counter == 0:
      self.core.statistics.updateDisplay(self.core.pygame)
      self.statistics_display_counter = 25
    else:
      self.statistics_display_counter = self.statistics_display_counter-1
  
  def runLifeCyclecounter(self):
    self.filecycle_counter = self.filecycle_counter-1
    self.lifecycle_now = False
    if self.filecycle_counter == 0:
      self.lifecycle_now = True
      self.filecycle_counter = Configuration.LILECYCLE_EACH_CYCLE
  
  def addObjectPositionInGrid(self, object):
    if object.carried_by == None:
      position = object.getPosition()
      if position in self.objects_positions_grid:
        self.objects_positions_grid[position].append(object)
      else:
        self.objects_positions_grid[position] = [object]
  
  def addNewObjectToSimulation(self, position, object, increase_statistics_data = True):
    if increase_statistics_data == True:
      self.core.statistics.increaseData(object.getId())
    self.placer.place(position, object)
  
  def deleteObjectFromSimulation(self, object):
    self.core.statistics.uncreaseData(object.getId())
    # TODO: Avoir un objetqui gere la suppression d'element
    for position in object.trace:
      self.core.pygame.colorizer.colorizePixel(position, (0,0,0))
    del object

  def findObjectNearPosition(self, object_class, position_ref, distance, allow_same_position):
    possibles_coordonates = get_near_coordonates_for_position(position_ref, distance, allow_same_position)
    
    for coordonate in possibles_coordonates:
      if coordonate in self.objects_positions_grid_previous_cycle:
        for object in self.objects_positions_grid_previous_cycle[coordonate]:
          if object.__class__.__name__ == object_class:
            return object

  def getObjects(self):
    # TODO: Il y a peut-etre confusion: on met actuellement les
    # objets termites dans TermiteSimulator. Or il faudrai que les
    # objets soit dans SimulationManager et que TermiteSimulator pioche
    # les objets termites dans les objets de la simulation
    return self.termites_simulator.termites
  
  def addZone(self, zone):
    self.zones[zone.id] = zone
  
  def addTraceZone(self, trace_zone, class_zone):
    if class_zone in self.trace_zones:
      self.trace_zones[class_zone].appendleft(trace_zone)
      if len(self.trace_zones[class_zone]) > Configuration.MAX_PLANTPIECE_ROADS:
        self.trace_zones[class_zone].pop()
    else:
      self.trace_zones[class_zone] = deque()
      self.trace_zones[class_zone].appendleft(trace_zone)
  
  def getZoneIfExist(self, zone_id):
    if zone_id in self.zones:
      return self.zones[zone_id]
    return None
  
  def positionIsInArea(self, zone_id, position):
    zone = self.getZoneIfExist(zone_id)
    if zone != None:
      if zone.positionIsInArea(position):
        return True
    return False
  
  def getDistanceFromArea(self, zone_id, position):
    zone = self.getZoneIfExist(zone_id)
    if zone != None:
      return zone.getDistanceFromAreaCenter(position)
    return None
  
  def positionIsInTrace(self, class_zone, position):
    if class_zone in self.trace_zones:
      for trace_zone in self.trace_zones[class_zone]:
        if trace_zone.positionIsInArea(position):
          return True
    return False
