import random

class Move(object):
  
  #object_parent = None
  direction = None
  
  def __init__(self):#, object_parent):
    #self.object_parent = object_parent
    self.determineDirection()
  
  # La direction prendra en compte des probabilite, ces probabilites seront
  # definis par l'objet enfant
  def determineDirection(self):
    self.direction = random.randint(1, 8)