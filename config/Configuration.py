class Configuration(object):
  
  CONF_WINDOWS_NAME = 'Termites Simulator'
  CONF_SCREEN_WIDTH = 640
  CONF_SCREEN_WIDTH_MIDDLE = 320
  CONF_SCREEN_HEIGHT = 480
  CONF_SCREEN_HEIGHT_MIDDLE = 240
  CONF_CLOCK_TICK = 25 # None is allowed, 25 for eye natural
  
  CONF_TERMITES_COUNT_WORKER_NOWORK = 50
  CONF_TERMITES_COUNT_WORKER_NURSING = 10
  
  """
  Position de zones
  """
  ZONE_NURSERY_POSITION = [320, 240]
  ZONE_NURSERY_RADIUS = 52
  
  """
  Regles pour les zones
  """
  # TODO: pas tre dynamique ca ...
  ZONE_RULE_JAIL = {
    'Queen' : 'Queening',
    'Worker' : 'Nursing'
  }
  
  ZONE_RULE_ACTION = {
    'PlantZone' : ['Worker_Fooding'],
    'PlantRepository' : ['Worker_Fooding']
  }
  
  """
    Deplacement des termites:
    
    MOVE_WAIT_PROBABILITY permet de donner un mouvement realiste a la termite, de facon a ce
    qu'elle fasse de petite pause de temps en temps (on donne la probabilite que la termite
    fasse une pause alors que'elle devait se deplacer)
    
    Lorsque SAME_WAY est a 1/1 et qu'on laisse faire SLIGHTLY_TURN on obtient un mouvement
    plus realiste. Les virage sont plus doux.
    Plus la probabilite de SLIGHTLY_TURN est faible, plus la termite s'eloigne vite
    
    Lorsque on utilise une proba sur SAME_WAY les virages sont plus casses
  """
  TERMITE_MOVE_WAIT_PROBABILITY = [2, 10]
  TERMITE_QUEEN_MOVE_WAIT_PROBABILITY = [99, 100]
  TERMITE_MOVE_DIRECTION_SAME_WAY_PROBABILITY = [1, 1]
  TERMITE_MOVING_SAME_WAY_SLIGHTLY_TURN_PROBABILITY = [1, 2]
  """ La reine pond un eouf tous les x cycles """
  TERMITE_QUEEN_LAY_EACH_CYCLE = 50
  
  """
    Cycles de vies
  """
  LILECYCLE_EACH_CYCLE = 25
  """ Duree de vie maximum """
  TERMITES_LIFETIMES = {
    'Worker' : 1800, # 900:15min
    'Larva' : 900
  }
  LARVA_HATCH_CYCLES = 420 # 300:5min
  LARVA_PUTTED_NEAR_LARVA_HATCH_BONUS = 175
  
  
  """
   GAMING DEFAUKT VALUES FOR PLAYER CONFIGURATION
  """
  COUNT_MAX_NURSES = 40
  # sur 100%
  QUEEN_LAY_PROBABILITY = {
    'Worker' : 100
  }
  # sur 100%
  """ TODO: 1 - comment faire propager les ordres ? (plus simpe, direct sur tt les termites)
      TODO: 2 - lorsque une termite a l'exterieur du cercle couffin devient nourice:
                il faut qu'elle puisse se deplacer jusqu'a la reine
                => Il faut lors du deplacement calculer si la direction va s'eloigner ou se
                rapprocher de la zone des couffins (utiliser le systeme matheu deja implemente).
  """
  WORKER_ORDER_NURSING = 10
  WORKER_ORDER_FOODING = 90
  
  CONFIGURATION_AND_PLAYER_WINDOW_RELATIONS = {
    'fps_max' : 'CONF_CLOCK_TICK',
    'count_max_nurses' : 'COUNT_MAX_NURSES',
    'worker_order_nursing' : 'WORKER_ORDER_NURSING',
    'worker_order_fooding' : 'WORKER_ORDER_FOODING'
  }
  
  def setConfiguration(self, configuration_id, configuration_value):
    setattr(self, configuration_id, configuration_value)