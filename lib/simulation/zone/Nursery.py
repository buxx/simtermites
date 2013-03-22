from lib.simulation.zone.Zone import Zone

class Nursery(Zone):
  
  def __init__(self, position, radius):
    # TODO: Il faudra pouvoir gerer plusieurs zone du meme type, donc avoir un id
    # plus persmissif
    Zone.__init__(self, position, radius, 'Nursery') 
