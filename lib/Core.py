from lib.mover.Mover import Mover
from lib.Pygame import Pygame
from lib.simulation.SimulationManager import SimulationManager
from lib.interaction.EventManager import EventManager

# TODO: Utiliser de vrai constantes (cf google)
CONF_WINDOWS_NAME = 'Termites Simulator'
CONF_SCREEN_WIDTH = 640
CONF_SCREEN_HEIGHT = 480
CONF_TERMITES_COUNT = 1000

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