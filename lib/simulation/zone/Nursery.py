from lib.simulation.zone.Zone import Zone

class Nursery(Zone):
  
  draw = True
  color = 255, 35, 244
  
  def __init__(self, position, radius):
    # TODO: Il faudra pouvoir gerer plusieurs zone du meme type, donc avoir un id
    # plus persmissif
    Zone.__init__(self, position, radius, 'Nursery') 
