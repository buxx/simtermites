class Restriction(object):
  
  simulation = None
  restrictions = {}
  
  def __init__(self, simulation):
    self.simulation = simulation
    self.updateRestrictions()
  
  def canDoAction(self, action_id, count_reference):
    if action_id in self.restrictions:
      if count_reference > self.restrictions[action_id]:
        return False
    return True
    
  def updateRestrictions(self):
    self.restrictions = {
      'Lay_Worker_Nursing' : self.simulation.core.configuration.COUNT_MAX_NURSES
    }
