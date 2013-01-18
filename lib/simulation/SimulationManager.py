from lib.entity.bug.termite.Worker import Worker as TermiteWorker
from config.Configuration import Configuration
from lib.simulation.TermitesSimulator import TermitesSimulator
from lib.ground.connector.Mover import Mover

class SimulationManager(object):
  
  core = None
  termites_simulator = None
  mover = None
  
  def __init__(self, Core):
    self.core = Core
    self.mover = Mover(self.core.pygame.screen)
    self.initializeBugs()
  
  def initializeBugs(self):
    termites_count = 1
    termites = []
    while termites_count <= Configuration.CONF_TERMITES_COUNT:
      termites.append(TermiteWorker((320, 240)))
      termites_count = termites_count+1
    
    self.termites_simulator = TermitesSimulator(self, termites)
  
  def runCycle(self):
    self.termites_simulator.runActions()
    self.core.updateDisplay()
    if (Configuration.CONF_CLOCK_TICK):
      self.core.pygame.clock.tick(Configuration.CONF_CLOCK_TICK)
  