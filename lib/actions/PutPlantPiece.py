from lib.actions.Put import Put

class PutPlantPiece(Put):
  
  def do(self):
    Put.do(self)
    self.brain.connectToTrace('PlantPiecesRoad', self.simulation, -1)
