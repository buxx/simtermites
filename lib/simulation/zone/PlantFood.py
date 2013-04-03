from lib.simulation.zone.CircleZone import CircleZone

class PlantFood(CircleZone):
  
  draw = True
  color = 0, 187, 5
  
  def __init__(self, position, radius):
    # TODO: Il faudra pouvoir gerer plusieurs zone du meme type, donc avoir un id
    # plus persmissif
    CircleZone.__init__(self, position, radius, 'PlantZone') 
