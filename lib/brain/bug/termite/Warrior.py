from lib.brain.bug.termite.Termite import Termite

class Warrior(Termite):
  
  def __init__(self, host):
    Termite.__init__(self, host)
  
  def getAction(self, simulation):
    # Actions d'une gerrieres
    return None