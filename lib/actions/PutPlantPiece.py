from lib.actions.Put import Put

class PutPlantPiece(Put):
  
  def do(self):
    Put.do(self)
    self.brain.connectToTrace('PlantPiecesRoad', self.simulation, -1)
    #print self.brain.trace_following
    #print self.brain.trace_following_point
    #print self.brain.trace_following_way
    #print 'TTTTT'