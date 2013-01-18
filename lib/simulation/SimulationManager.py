from lib.mover.Mover import Mover
from lib.entity.bug.termite.Worker import Worker as TermiteWorker

# TODO: Utiliser de vrai constantes (cf google)
CONF_WINDOWS_NAME = 'Termites Simulator'
CONF_SCREEN_WIDTH = 640
CONF_SCREEN_HEIGHT = 480
CONF_TERMITES_COUNT = 1000

class SimulationManager(object):
  
  core = None
  # TODO: pour tes tests preleminaire, ensuite ce donnees seront dans un objet specialise
  termites = []
  mover = None # pareil pour mover ?
  
  def __init__(self, Core):
    self.core = Core
    termites = 1
    self.termites = []
    while termites <= CONF_TERMITES_COUNT:
      self.termites.append(TermiteWorker((20, 20)))
      termites = termites+1
    self.mover = Mover(self.core.pygame.screen)
  
  def runCycle(self):
    for termite in self.termites:
      self.mover.move(termite)
      
    self.core.pygame.display_update()
    self.core.pygame.clock.tick(25)