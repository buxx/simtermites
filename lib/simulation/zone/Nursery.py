from lib.simulation.zone.CircleZone import CircleZone

class Nursery(CircleZone):
  
  draw = True
  color = 255, 35, 244
  
  def __init__(self, position, radius):
    # TODO: Il faudra pouvoir gerer plusieurs zone du meme type, donc avoir un id
    # plus persmissif
    CircleZone.__init__(self, position, radius, 'Nursery') 
