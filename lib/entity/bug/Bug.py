from lib.entity.ObjectAlive import ObjectAlive

class Bug(ObjectAlive):
  
  def __init__(self, brain, length):
    ObjectAlive.__init__(self, brain, length)