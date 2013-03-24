# TODO: utiliser pygame (a nous) pour crer le font
import pygame

class Statistics(object):
  
  objects = {}
  hidden_objects = {}
  
  def __init__(self):
    pass
  
  def getObjects(self, hidden = False):
    if hidden == False:
      return self.objects
    return self.hidden_objects
  
  def setObjects(self, objects, hidden = False):
    if hidden == False:
      self.objects = objects
    self.hidden_objects = objects
  
  def getData(self, data_id, hidden = False, return_zero_if_none = False):
    objects = self.getObjects(hidden)
    if data_id in objects:
      return objects[data_id]
    if return_zero_if_none == False:
      return None
    return 0
  
  def increaseData(self, data_id, hidden = False):
    objects = self.getObjects(hidden)
    if data_id in objects:
      objects[data_id] = objects[data_id]+1
    else:
      objects[data_id] = 1
    self.setObjects(objects, hidden)
  
  def uncreaseData(self, data_id, hidden = False):
    objects = self.getObjects(hidden)
    if data_id in objects:
      objects[data_id] = objects[data_id]-1
    self.setObjects(objects, hidden)
  
  def updateDisplay(self, pygame_):
    pos_y = 2
    for data_id in self.objects:
      pygame_.draw_rect((175, 175, 175), (2,pos_y, 170 , 12), 0)
      label = pygame_.getLabel(data_id+': '+str(self.objects[data_id]))
      pygame_.screen.blit(label, (2, pos_y))
      pos_y = pos_y + 12
