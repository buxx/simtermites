# TODO: utiliser pygame (a nous) pour crer le font
import pygame

class Statistics(object):
  
  objects = {}
  
  def __init__(self):
    pass
  
  def getData(self, data_id):
    if data_id in self.objects:
      return self.objects[data_id]
    return None
  
  def increaseData(self, data_id):
    if data_id in self.objects:
      self.objects[data_id] = self.objects[data_id]+1
    else:
      self.objects[data_id] = 1
  
  def uncreaseData(self, data_id):
    if data_id in self.objects:
      self.objects[data_id] = self.objects[data_id]-1
  
  def updateDisplay(self, pygame_):
    pos_y = 2
    for data_id in self.objects:
      pygame_.draw_rect((175, 175, 175), (2,pos_y, 115 ,11), 0)
      label = pygame_.getLabel(data_id+': '+str(self.objects[data_id]))
      pygame_.screen.blit(label, (2, pos_y))
      pos_y = pos_y + 12