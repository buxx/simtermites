from config.Configuration import Configuration

class Restriction(object):
  
  simulation = None
  restrictions = {
    'Lay_Worker_Nursing' : Configuration.COUNT_MAX_NURSES
  }
  
  def __init__(self, simulation):
    self.simulation = simulation
  
  def canDoAction(self, action1, action2):
    if action1+'_'+action2 in self.restrictions and self.simulation.core.statistics.getData(action2) != None:
      print 'action connu'
      print str(self.simulation.core.statistics.getData(action2)) + ' ' + str(self.restrictions[action1+'_'+action2])
      if self.simulation.core.statistics.getData(action2) > self.restrictions[action1+'_'+action2]:
        return False
    return True
