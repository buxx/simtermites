from lib.simulation.zone.CircleZone import CircleZone

class PlantRepository(CircleZone):
  
  draw = True
  color = 130, 130, 130
  
  def __init__(self, position, radius):
    # TODO: Il faudra pouvoir gerer plusieurs zone du meme type, donc avoir un id
    # plus persmissif
    CircleZone.__init__(self, position, radius, 'PlantRepository') 
