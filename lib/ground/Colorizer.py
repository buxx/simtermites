class Colorizer(object):
  
  screen = None
  
  def __init__(self, screen):
    self.screen = screen

  def colorizePixel(self, position, color):
    self.screen.set_at(position, color)