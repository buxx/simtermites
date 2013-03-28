from lib.Pygame import Pygame
from lib.simulation.SimulationManager import SimulationManager
from lib.interaction.EventManager import EventManager
from lib.tool.Satistics import Statistics
from lib.tool.PlayerWindow import PlayerWindow
from config.Configuration import Configuration

import pygtk
pygtk.require('2.0')
import gtk

class Core(object):
  """"""
  
  pygame = None
  simulation = None
  event_manager = None
  statistics = None
  player_configuration = None
  configuration = None
  
  def start(self):
    
    self.configuration = Configuration()
    self.initialize_pygame()
    self.initialyze_event_manager()
    self.statistics = Statistics()
    self.initialyze_simulation()
    
    self.player_configuration = PlayerWindow(self)
    self.player_configuration.start()
    
    run_simulation = True
    try:
      while run_simulation:
        run_simulation = self.event_manager.listenAndPropagate()
        self.simulation.runCycle()
    except KeyboardInterrupt:
      pass
    
    self.player_configuration._Thread__stop()
    
  def initialize_pygame(self):
    self.pygame = Pygame()
  
  def initialyze_event_manager(self):
    self.event_manager = EventManager(self)
    
  def initialyze_simulation(self):
    self.simulation = SimulationManager(self)
    
  def updateDisplay(self):
    self.pygame.display_update()
  
  def updateConfiguration(self, player_configurations):
    for key in player_configurations:
      self.configuration.setConfiguration(self.configuration.CONFIGURATION_AND_PLAYER_WINDOW_RELATIONS[key], player_configurations[key])
    self.simulation.restriction.updateRestrictions()
