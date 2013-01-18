class Configuration(object):
  
  CONF_WINDOWS_NAME = 'Termites Simulator'
  CONF_SCREEN_WIDTH = 640
  CONF_SCREEN_HEIGHT = 480
  CONF_TERMITES_COUNT = 1000
  CONF_CLOCK_TICK = 25
  
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