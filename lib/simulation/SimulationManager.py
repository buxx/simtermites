from lib.mover.Mover import Mover
from lib.entity.bug.termite.Worker import Worker as TermiteWorker
from config.Configuration import Configuration

class SimulationManager(object):
  
  core = None
  # TODO: pour tes tests preleminaire, ensuite ce donnees seront dans un objet specialise
  termites = []
  mover = None # pareil pour mover ?
  
  def __init__(self, Core):
    self.core = Core
    termites = 1
    self.termites = []
    while termites <= Configuration.CONF_TERMITES_COUNT:
      self.termites.append(TermiteWorker((320, 240)))
      termites = termites+1
    self.mover = Mover(self.core.pygame.screen)
  
  def runCycle(self):
    for termite in self.termites:
      self.mover.move(termite)
      
    self.core.pygame.display_update()
    if (Configuration.CONF_CLOCK_TICK):
      self.core.pygame.clock.tick(Configuration.CONF_CLOCK_TICK)