class Zone(object):
  
  id = ''
  draw = False
  color = None
  
  def __init__(self, zone_id):
    self.id = zone_id
  
  def positionIsInArea(self, tested_position):
    raise('You must implement this')
