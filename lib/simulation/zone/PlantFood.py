from lib.simulation.zone.Zone import Zone

class PlantFood(Zone):
  
  draw = True
  color = 0, 187, 5
  
  def __init__(self, position, radius):
    # TODO: Il faudra pouvoir gerer plusieurs zone du meme type, donc avoir un id
    # plus persmissif
    Zone.__init__(self, position, radius, 'PlantZone') 
