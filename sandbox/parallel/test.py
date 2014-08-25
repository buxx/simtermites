import sys

if sys.version_info < (3, 3):
  sys.stdout.write("Python 3.3 required\n")
  sys.exit(1)

from multiprocessing import Process, Pipe
from multiprocessing.connection import wait
from processmanager import ProcessManager

def do_things_in_process(things_to_do = []):
  return [i ** 12 for i in things_to_do] 

process_manager = ProcessManager(2, do_things_in_process)
print(process_manager.get_their_work([0,1,2,3]))
print(process_manager.get_their_work([0,1,2,3]))
process_manager.stop()

process_manager = ProcessManager(2, do_things_in_process)
print(process_manager.get_their_work([4,5,6,7]))
print(process_manager.get_their_work([4,5,6,7]))
process_manager.stop()