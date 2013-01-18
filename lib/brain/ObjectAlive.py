from lib.brain.Brain import Brain

class ObjectAlive(Brain):
  
  def __init__(self, host):
    Brain.__init__(self, host)
    
  def think(self):
    raise Exception("Cette methode doit etre implemente par un objet enfant")