from lib.entity.bug.Bug import Bug

class Termite(Bug):
  
  color = 255, 240, 200
  
  def __init__(self, brain, pos, length):
    Bug.__init__(self, brain, pos, length)