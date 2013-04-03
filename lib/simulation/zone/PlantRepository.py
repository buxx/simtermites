from lib.simulation.zone.Zone import Zone

class PlantRepository(Zone):
  
  draw = True
  color = 130, 130, 130
  
  def __init__(self, position, radius):
    # TODO: Il faudra pouvoir gerer plusieurs zone du meme type, donc avoir un id
    # plus persmissif
    Zone.__init__(self, position, radius, 'PlantRepository') 
