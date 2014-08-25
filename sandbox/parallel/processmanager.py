import sys

if sys.version_info < (3, 3):
  sys.stdout.write("Python 3.3 required\n")
  sys.exit(1)

from multiprocessing import Process, Pipe
from multiprocessing.connection import wait

class ProcessManager(object):
  def __init__(self, nb_process, target):
    self.processs = []
    self.target = target
    self.nb_process = nb_process
    self.readers_pipes = []
    self.writers_pipes = []
  def _start(self, things_to_do):
    for i in range(self.nb_process):
      local_read_pipe, local_write_pipe = Pipe(duplex=False)
      process_read_pipe, process_write_pipe = Pipe(duplex=False)
      self.readers_pipes.append(local_read_pipe)
      self.writers_pipes.append(process_write_pipe)
      p = Process(target=run_process, args=(self.target, local_write_pipe, process_read_pipe, things_to_do))
      p.start()
      self.processs.append(p)
      local_write_pipe.close()
      process_read_pipe.close()
  def stop(self):
    for writer_pipe in self.writers_pipes:
      writer_pipe.send('stop')
  
  def get_their_work(self, things_to_do):
    if not self.processs:
      self._start(things_to_do)
    else:
      for writer_pipe in self.writers_pipes:
        print('send things')
        writer_pipe.send(things_to_do)
    things_done_collection = []
    reader_useds = []
    while self.readers_pipes:
      for r in wait(self.readers_pipes):
        try:
          things_dones = r.recv()
        except EOFError:
          reader_useds.append(r)
          self.readers_pipes.remove(r)
        else:
          reader_useds.append(r)
          self.readers_pipes.remove(r)
          things_done_collection.append(things_dones)
    self.readers_pipes = reader_useds
    return things_done_collection

def run_process(target, main_write_pipe, process_read_pipe, things):
  things_dones = target(things)
  main_write_pipe.send(things_dones)
  
  new_things = None
  readers = [process_read_pipe]
  readers_used = []
  while readers:
    for r in wait(readers):
      try:
        new_things = r.recv()
        print('p: things received')
      except EOFError:
        pass
      finally:
        readers.remove(r)
  print('p: continue')
  if new_things != 'stop':
    run_process(target, main_write_pipe, process_read_pipe, new_things)
