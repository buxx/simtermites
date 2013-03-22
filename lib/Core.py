from lib.Pygame import Pygame
from lib.simulation.SimulationManager import SimulationManager
from lib.interaction.EventManager import EventManager
from lib.tool.Satistics import Statistics

class Core(object):
  """"""
  
  pygame = None
  simulation = None
  event_manager = None
  statistics = None
  
  def start(self):
    
    self.initialize_pygame()
    self.initialyze_event_manager()
    self.statistics = Statistics()
    self.initialyze_simulation()
    
    run_simulation = True
    while run_simulation:
      run_simulation = self.event_manager.listenAndPropagate()
      self.simulation.runCycle()
      
  def initialize_pygame(self):
    self.pygame = Pygame()
  
  def initialyze_event_manager(self):
    self.event_manager = EventManager(self)
    
  def initialyze_simulation(self):
    self.simulation = SimulationManager(self)
    
  def updateDisplay(self):
    self.pygame.display_update()