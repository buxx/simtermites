from lib.actions.Action import Action
from config.Configuration import Configuration
import random
from config.Configuration import Configuration
from lib.simulation.ZoneConnector import ZoneConnector

class Move(Action):
  
  direction = None
  new_coordonates = None
  brain = None
    
  direction_same_way_probability = None
  same_way_slightly_turn_probability = None
  
  def __init__(self, simulation, brain):
    Action.__init__(self, simulation, brain)
    self.determineDirection()
  
  def do(self):
    self.simulation.mover.move(self.brain.host, self)
    self.brain.host.hasMoved(self.new_coordonates)
  
  def determineDirection(self, refused_coordonates_count = 0):
    self.getNewDirection()
    if not self.canMoveInThisCoordonates(self.new_coordonates, refused_coordonates_count):
      self.direction_same_way_probability = [0,100]
      self.determineDirection(refused_coordonates_count+1)
  
  def canMoveInThisCoordonates(self, new_coordonates, refused_coordonates_count):
    
    # sortie d'ecran: TODO dans un fct seule
    if new_coordonates[0] < 0 or new_coordonates[1] < 0 or new_coordonates[0] > Configuration.CONF_SCREEN_WIDTH or new_coordonates[1] > Configuration.CONF_SCREEN_HEIGHT:
      return False
    
    if ZoneConnector.objectMatchWithJailZone(self.brain.host.__class__.__name__, self.brain.work, 'Nursery'):
      nursery = self.simulation.getZoneIfExist('Nursery')
      if nursery != None :
        if not nursery.positionIsInArea(new_coordonates):
          return False
    # TODO: Modifier ce code hardcoded. Il faut changer le ZONE_RULE_JAIL pour preciser
    # la zone en question
    if self.brain.host.__class__.__name__ == 'Worker' and\
       self.brain.work == 'Fooding' and\
       self.brain.host.canCarryObject() == True:
      if self.brain.host.object_carried != None:
        if self.brain.host.object_carried.__class__.__name__ == 'PlantPiece':
          
          #### TMP
          # if in Fortress, plus de route a suivre!
          if self.simulation.positionIsInArea('Fortress', self.brain.host.getPosition()):
            self.brain.stopFollowingRoute()
          
          # sors de PlantRepository
          if not self.simulation.positionIsInArea('PlantRepository', new_coordonates) and self.simulation.positionIsInArea('PlantRepository', self.brain.host.getPosition()):
            return False
          else:
            # dans forteresse mais pas dans PlantRepository
            if self.simulation.positionIsInArea('Fortress', self.brain.host.getPosition()) and not self.simulation.positionIsInArea('PlantRepository', self.brain.host.getPosition()):
              # s'eloigne de PlantRepository
              if self.simulation.getDistanceFromArea('PlantRepository', new_coordonates) > self.simulation.getDistanceFromArea('PlantRepository', self.brain.host.getPosition()):
                return False
            else:
              # s'eloigne de PlantPiecesRoad
              # todo: s'eloigne de prochain point de la trace
              #if not self.simulation.positionIsInTrace('PlantPiecesRoad', new_coordonates) and self.simulation.positionIsInTrace('PlantPiecesRoad', self.brain.host.getPosition()):
              if self.isGoingAwayFromRoad(new_coordonates):
                return False
              # n'est pas dans PlantRepository
              elif not self.simulation.positionIsInArea('PlantRepository', self.brain.host.getPosition()):
                # s'eloigne de Fortress
                if self.simulation.getDistanceFromArea('Fortress', new_coordonates) > self.simulation.getDistanceFromArea('Fortress', self.brain.host.getPosition()) and refused_coordonates_count < 3:
                  return False
      
      else:
        
        # test si pas de soute suivis, on en demande une afin que toutes les termites aille dans ces traces!
        if self.brain.noTraceFollowingSinceTooLong():
          self.brain.connectToTrace('PlantPiecesRoad', self.simulation, -1)
        
        #if not self.simulation.positionIsInTrace('PlantPiecesRoad', new_coordonates) and self.simulation.positionIsInTrace('PlantPiecesRoad', self.brain.host.getPosition()):
        # s'eloigne du prochain point de la trace
        if self.isGoingAwayFromRoad(new_coordonates):
          return False
    return True
  
  def isGoingAwayFromRoad(self, new_coordonates):
    if self.brain.trace_following != None:
      point = self.brain.trace_following.coordonates[self.brain.trace_following_point]
      
      # Palliatif: Il arrive que la position actuelle soir a 0 de distance du point objectif.
      # bizarrement on est pas passe au point suivant, du coup on le fait de force maintenant
      if self.brain.trace_following.getDistanceFromPoint(self.brain.host.getPosition(), point) == 0:
        self.brain.aimForNextPointInRoad()
        return self.isGoingAwayFromRoad(new_coordonates)
      # 
      
      if self.brain.trace_following.getDistanceFromPoint(new_coordonates, point) > self.brain.trace_following.getDistanceFromPoint(self.brain.host.getPosition(), point):
        return True
    return False
  
  def getNewDirection(self):
    if self.takeSameDirection():
      if self.isSlightlyTurn():
        self.direction = self.getSlightlyTurn(self.brain.host.last_direction)
        self.brain.host.last_direction = self.direction
      else:
        self.direction = self.brain.host.last_direction
    else:
      self.direction = random.randint(0, 7)
      self.brain.host.last_direction = self.direction
    self.new_coordonates = self.movePixel(self.brain.host.getPosition(), self.direction)
  
  def takeSameDirection(self):
    randomint = random.randint(1, self.direction_same_way_probability[1])
    if randomint >= 1 and randomint <= self.direction_same_way_probability[0] \
       and self.brain.host.last_direction != None :
      return True
    return False
  
  def isSlightlyTurn(self):
    randomint = random.randint(1, self.same_way_slightly_turn_probability[1])
    if randomint >= 1 and randomint <= self.same_way_slightly_turn_probability[0]:
      return True
    return False
  
  def getSlightlyTurn(self, last_direction):
    randomint = random.randint(last_direction-1, last_direction+1)
    if randomint == -1:
      randomint = 7
    if randomint == 8:
      randomint = 0
    return randomint
  
  def movePixel(self, pos, direction):
    x = pos[0]
    y = pos[1]
    
    if direction == 0:
      x = x+1
    if direction == 1:
      x = x+1
      y = y+1
    if direction == 2:
      y = y+1
    if direction == 3:
      x = x-1
      y = y+1
    if direction == 4:
      x = x-1
    if direction == 5:
      x = x-1
      y = y-1
    if direction == 6:
      y = y-1
    if direction == 7:
      x = x+1
      y = y-1
    
    return (int(x), int(y))
