from lib.actions.Move.Move import Move
from config.Configuration import Configuration

class Termite(Move):
  
  def __init__(self, simulation, brain):
    self.direction_same_way_probability = Configuration.TERMITE_MOVE_DIRECTION_SAME_WAY_PROBABILITY
    self.same_way_slightly_turn_probability = Configuration.TERMITE_MOVING_SAME_WAY_SLIGHTLY_TURN_PROBABILITY
    Move.__init__(self, simulation, brain)
  