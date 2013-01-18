from lib.brain.bug.termite.Termite import Termite

class Worker(Termite):
  
  def __init__(self, host):
    Termite.__init__(self, host)