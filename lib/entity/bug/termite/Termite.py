from lib.entity.bug.Bug import Bug

class Termite(Bug):
  
  def __init__(self, pos, length):
    Bug.__init__(self, pos, length)