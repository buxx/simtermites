import sys

from multiprocessing import Process, Pipe
from multiprocessing.connection import wait
from processmanager import KeepedAliveProcessManager, ProcessManager
from random import choice
import timeit

class Bug(object):
  def __init__(self, id):
    self.id = id
    self.willmove = None

class SimpleWorker(object):
  def __init__(self, bugs):
    self.bugs = bugs
  def action_them(self):
    for bug in self.bugs:
      self.action_him(bug)
  def action_him(self, bug):
    bug.willmove = choice(range(9))

def run_worker(bugs):
  worker = SimpleWorker(bugs)
  worker.action_them()
  return worker.bugs

n=100000
bugs = []
for i in range(n):   
  bugs.append(Bug(i))

def compute_keep_alive(bugs, nb_process=1, repeat=1):
  process_manager = KeepedAliveProcessManager(nb_process, run_worker)
  for i in range(repeat):
    process_manager.get_their_work(bugs)
  process_manager.stop()

def compute_recreate(bugs, nb_process=1, repeat=1):
  process_manager = ProcessManager(nb_process, run_worker)
  for i in range(repeat):
    process_manager.get_their_work(bugs)

max_process = '4'

print('keep: 1 processs, 01 cycles: ', timeit.timeit('compute_keep_alive(bugs, nb_process=1, repeat=1)',\
                                                     number=1,\
                                                     setup='from __main__ import bugs,Bug,SimpleWorker,compute_keep_alive'))
print('recr: 1 processs, 01 cycles: ', timeit.timeit('compute_recreate(bugs, nb_process=1, repeat=1)',\
                                                     number=1,\
                                                     setup='from __main__ import bugs,Bug,SimpleWorker,compute_recreate'))

print('keep: 1 processs, 25 cycles: ', timeit.timeit('compute_keep_alive(bugs, nb_process=1, repeat=25)',\
                                                     number=1,\
                                                     setup='from __main__ import bugs,Bug,SimpleWorker,compute_keep_alive'))
print('recr: 1 processs, 25 cycles: ', timeit.timeit('compute_recreate(bugs, nb_process=1, repeat=25)',\
                                                     number=1,\
                                                     setup='from __main__ import bugs,Bug,SimpleWorker,compute_recreate'))

print('keep: '+max_process+' processs, 01 cycles: ', timeit.timeit('compute_keep_alive(bugs, nb_process='+max_process+', repeat=1)',\
                                                     number=1,\
                                                     setup='from __main__ import bugs,Bug,SimpleWorker,compute_keep_alive'))
print('recr: '+max_process+' processs, 01 cycles: ', timeit.timeit('compute_recreate(bugs, nb_process='+max_process+', repeat=1)',\
                                                     number=1,\
                                                     setup='from __main__ import bugs,Bug,SimpleWorker,compute_recreate'))

print('keep: '+max_process+' processs, 25 cycles: ', timeit.timeit('compute_keep_alive(bugs, nb_process='+max_process+', repeat=25)',\
                                                     number=1,\
                                                     setup='from __main__ import bugs,Bug,SimpleWorker,compute_keep_alive'))
print('recr: '+max_process+' processs, 25 cycles: ', timeit.timeit('compute_recreate(bugs, nb_process='+max_process+', repeat=25)',\
                                                     number=1,\
                                                     setup='from __main__ import bugs,Bug,SimpleWorker,compute_recreate'))





