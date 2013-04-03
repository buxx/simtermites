from lib.brain.bug.termite.Termite import Termite
from lib.actions.Take import Take
from lib.actions.TakePlantPiece import TakePlantPiece
from lib.actions.PutLarva import PutLarva
from lib.actions.PutPlantPiece import PutPlantPiece


from lib.simulation.ZoneConnector import ZoneConnector

class Worker(Termite):

  def __init__(self, host, work = None):
    Termite.__init__(self, host)
    self.work = work
  
  def getAction(self, simulation):
    
    if self.work == 'Nursing':
      # TODO: il faudra passer un tableau de types d'objet
      # pour ne faire cette demande qu'une seule fois
      larva_near = simulation.findObjectNearPosition('Larva', self.host.getPosition(), 1, False)
      if larva_near != None:
        if self.host.object_carried == None:
          return Take(simulation, self, self.host, larva_near)
        elif self.host.object_carried.__class__.__name__ == 'Larva':
          return PutLarva(simulation, self, self.host, self.host.object_carried)
    
    if self.work =='Fooding':
      if ZoneConnector.objectMatchWithActionZone('Worker', 'Fooding', 'PlantZone'):
        # TODO: ce code ne permet qu'une zone de ce type, il faudra
        # recup une liste et regarder si il est dans une d'entre elles
        plant_zone = simulation.getZoneIfExist('PlantZone')
        if plant_zone != None :
          if plant_zone.positionIsInArea(self.host.getPosition()):
            if self.host.object_carried == None:
              return TakePlantPiece(simulation, self, self.host)
      if ZoneConnector.objectMatchWithActionZone('Worker', 'Fooding', 'PlantRepository'):
        # TODO: ce code ne permet qu'une zone de ce type, il faudra
        # recup une liste et regarder si il est dans une d'entre elles
        plant_repo = simulation.getZoneIfExist('PlantRepository')
        if plant_repo != None :
          if plant_repo.positionIsInArea(self.host.getPosition()):
            if self.host.object_carried != None:
              if self.host.object_carried.__class__.__name__ == 'PlantPiece':
                plant_piece_near = simulation.findObjectNearPosition('PlantPiece', self.host.getPosition(), 1, False)
                if plant_piece_near != None:
                  return PutPlantPiece(simulation, self, self.host, self.host.object_carried)
    return None
