from config.Configuration import Configuration

class Restriction(object):
  
  simulation = None
  restrictions = {
    'Lay_Worker_Nursing' : Configuration.COUNT_MAX_NURSES
  }
  
  def __init__(self, simulation):
    self.simulation = simulation
  
  def canDoAction(self, action_id, count_reference):
    if action_id in self.restrictions:
      if count_reference > self.restrictions[action_id]:
        return False
    return True
  
  def updateRestrictionParametersWithPlayerConfiguration(self, player_configurations):
    if 'count_max_nurses' in player_configurations:
      self.restrictions['Lay_Worker_Nursing'] = player_configurations['count_max_nurses']
