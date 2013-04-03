from lib.simulation.zone.CircleZone import CircleZone

class Fortress(CircleZone):
  
  draw = True
  color = 0, 23, 139
  
  def __init__(self, position, radius):
    # TODO: Il faudra pouvoir gerer plusieurs zone du meme type, donc avoir un id
    # plus persmissif
    CircleZone.__init__(self, position, radius, 'Fortress') 
