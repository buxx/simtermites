from lib.actions.Put import Put

class PutLarva(Put):
  
  def do(self):
    self.good.puttedNearLarva()
    Put.do(self)
