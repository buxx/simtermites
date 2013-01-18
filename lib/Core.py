from lib.mover.Mover import Mover
from lib.Pygame import Pygame
from lib.simulation.SimulationManager import SimulationManager
from lib.interaction.EventManager import EventManager

class Core(object):
  """"""
  
  pygame = None
  simulation = None
  event_manager = None
  
  def start(self):
    self.initialize_pygame()
    self.initialyze_event_manager()
    self.initialyze_simulation()
    run_simulation = True
    
    while run_simulation:
      run_simulation = self.event_manager.listenAndPropagate()
      self.simulation.runCycle()
      
  def initialize_pygame(self):
    self.pygame = Pygame()
    
  def initialyze_simulation(self):
    self.simulation = SimulationManager(self)
  
  def initialyze_event_manager(self):
    self.event_manager = EventManager(self)
    
  def updateDisplay(self):
    self.pygame.display_update()