from config.Configuration import Configuration
from lib.simulation.TermitesSimulator import TermitesSimulator
from lib.ground.connector.Mover import Mover
from lib.ground.connector.Placer import Placer
from lib.entity.bug.termite.Worker import Worker as TermiteWorker
from lib.entity.bug.termite.Queen import Queen as TermiteQueen

class SimulationManager(object):
  
  core = None
  termites_simulator = None
  mover = None
  placer = None
  
  def __init__(self, Core):
    self.core = Core
    self.mover = Mover(self.core.pygame.screen)
    self.placer = Placer(self.core.pygame.screen, self)
    self.initializeBugs()
  
  def initializeBugs(self):
    self.termites_simulator = TermitesSimulator(self, [])
    termites_count = 1
    while termites_count <= Configuration.CONF_TERMITES_COUNT:
      pos = (320, 240)
      self.placer.place(pos, TermiteWorker(pos))
      termites_count = termites_count+1
    self.placer.place((320, 240), TermiteQueen((320, 240)))
  
  def runCycle(self):
    self.termites_simulator.runActions()
    self.core.updateDisplay()
    if (Configuration.CONF_CLOCK_TICK):
      self.core.pygame.clock.tick(Configuration.CONF_CLOCK_TICK)
  