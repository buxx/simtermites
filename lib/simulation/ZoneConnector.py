from config.Configuration import Configuration

class ZoneConnector(object):
  
  @staticmethod
  def objectMatchWithJailZone(object_class, work, zone_name):
    if object_class in Configuration.ZONE_RULE_JAIL:
      if Configuration.ZONE_RULE_JAIL[object_class] == work:
        return True
    return False
