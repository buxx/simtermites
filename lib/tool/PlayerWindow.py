import threading
import gtk
import gtk.gdk
from config.Configuration import Configuration

gtk.gdk.threads_init()

class PlayerWindow(threading.Thread):
  
  core = None
  _stopevent = threading.Event()
  count_max_nurses_entry = None
  fps_max_entry = None
  player_configurations = {}
  
  def __init__(self, core):
    self.core = core
    threading.Thread.__init__(self)
  
  def run(self):
    self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    self.window.show()
    self.window.connect("delete_event", self.delete_event)
    
    self.vbox = gtk.VBox(False, 0)
    self.window.add(self.vbox)
    self.vbox.show()
    
    self.addEntrys()
    
    self.button = gtk.Button('Save values')
    self.button.connect("clicked", self.updatePlayerConfigurations)
    self.vbox.pack_start(self.button, True, True, 0)
    self.button.show()
    
    self.updatePlayerConfigurations(None, None, False)
    
    gtk.main()
    
  def addEntrys(self):
    self.addFPSMaxEntry()
    self.addCountMaxNursesEntry()

  def addFPSMaxEntry(self):
    self.fps_max_label = gtk.Label("FPS max")
    self.fps_max_entry = gtk.Entry()
    self.fps_max_entry.set_max_length(4)
    self.fps_max_entry.set_text(str(Configuration.CONF_CLOCK_TICK))
    self.vbox.pack_start(self.fps_max_label, True, True, 0)
    self.vbox.pack_start(self.fps_max_entry, True, True, 0)
    self.fps_max_entry.show()
    self.fps_max_label.show()
    
  def addCountMaxNursesEntry(self):
    self.count_max_nurses_label = gtk.Label("Nurses max")
    self.count_max_nurses_entry = gtk.Entry()
    self.count_max_nurses_entry.set_max_length(4)
    self.count_max_nurses_entry.set_text(str(Configuration.COUNT_MAX_NURSES))
    self.vbox.pack_start(self.count_max_nurses_label, True, True, 0)
    self.vbox.pack_start(self.count_max_nurses_entry, True, True, 0)
    self.count_max_nurses_entry.show()
    self.count_max_nurses_label.show()
  
  def updatePlayerConfigurations(self, widget = None, data = None, update_core = True):
    self.player_configurations['count_max_nurses'] = int(self.count_max_nurses_entry.get_text())
    self.player_configurations['fps_max'] = int(self.fps_max_entry.get_text())
    if update_core:
      self.core.updateConfiguration(self.player_configurations)
  
  def delete_event(self, widget, event, data=None):
    return True
  
  def getValue(self, value_id):
    if value_id in self.player_configurations:
      return self.player_configurations[value_id]
    return None
