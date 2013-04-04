from lib.brain.bug.termite.Termite import Termite
from lib.actions.Take import Take
from lib.actions.TakePlantPiece import TakePlantPiece
from lib.actions.PutLarva import PutLarva
from lib.actions.PutPlantPiece import PutPlantPiece
from lib.tool.TraceManipulator import TraceManipulator

from lib.simulation.ZoneConnector import ZoneConnector
from lib.simulation.zone.PlantPiecesTrace import PlantPiecesTrace

from collections import deque

class Worker(Termite):

  # tmp optimisation suivis trace
  trace_following = None
  trace_following_point = None
  
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
              # TEST
              #simulation.core.pygame.draw_pixels((130, 130, 130), TraceManipulator.getEnlargedTrace(self.host.long_trace, 10))
              simulation.addTraceZone(PlantPiecesTrace(self.host.long_trace, 10, 'TODO: id ou pas ici ?'), 'PlantPiecesRoad')
              self.host.long_trace = deque()
              # END TEST
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
  
  def connectToTrace(self, trace_class, simulation):
    current_distance = None
    current_point = None
    current_trace = None
    if trace_class in simulation.trace_zones:
      for trace_zone in simulation.trace_zones[trace_class]:
        for point in trace_zone.coordonates:
          distance_from_point = trace_zone.getDistanceFromPoint(self.host.getPosition(), point)
          if distance_from_point < current_distance or current_distance == None:
            current_distance = distance_from_point
            current_point = trace_zone.coordonates.index(point)
            current_trace = trace_zone
    self.trace_following = current_trace
    self.trace_following_point = current_point
    self.checkRoadProgress()
  
  def checkRoadProgress(self):
    if self.trace_following != None:
      point = self.trace_following.coordonates[self.trace_following_point]
      if self.trace_following.positionIsNearPoint(self.host.getPosition(), point):
        self.aimForNextPointInRoad()
  
  def aimForNextPointInRoad(self):
    if self.trace_following_point+1 in self.trace_following.coordonates:
      self.trace_following_point += 1
    else:
      self.trace_following_point = None
      self.trace_following = None
