from lib.brain.Brain import Brain
from lib.actions.Move import Move

class ObjectAlive(Brain):
  
  def __init__(self):
    Brain.__init__(self)
    
  def think(self):
    # Pour le moment on ne pense qu'a se deplacer
    return Move()