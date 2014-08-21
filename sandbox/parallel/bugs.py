import sys

if sys.version_info < (3, 3):
  sys.stdout.write("Python 3.3 required\n")
  sys.exit(1)

from itertools import permutations
from multiprocessing import Process, Pipe, current_process
from multiprocessing.connection import wait
from random import choice
from multiprocessing import Pool
import timeit

def chunk(seq,m):
   i,j,x=len(seq),0,[]
   for k in range(m):
     a, j = j, j + (i+k)//m
     x.append(seq[a:j])
   return x

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

def run_worker(w, bugs):
  worker = SimpleWorker(bugs)
  worker.action_them()
  w.send(worker.bugs)

def computer(bugs, nb_process=4):
  bugs_iterables = chunk(bugs, nb_process)  
  readers = []
  for i in range(nb_process):
    r, w = Pipe(duplex=False)
    readers.append(r)
    p = Process(target=run_worker, args=(w, bugs_iterables[i]))
    p.start()
    w.close()
  
  while readers:
    for r in wait(readers):
      try:
        bugs_sendeds = r.recv()
      except EOFError:
        readers.remove(r)
      else:
        for bug in bugs_sendeds:
          pass#print(bug.id, bug.willmove)

def compute(bugs, nb_process=4, cycles=1):
  for i in range(cycles):
    computer(bugs=bugs, nb_process=nb_process)

n=25000
bugs = []
for i in range(n):   
  bugs.append(Bug(i))

print('4 processs, 01 cycles: ', timeit.timeit('compute(bugs, nb_process=4)', number=10, setup='from __main__ import bugs,chunk,Bug,SimpleWorker,run_worker,computer,compute'))
print('1 processs, 01 cycles: ', timeit.timeit('compute(bugs, nb_process=1)', number=10, setup='from __main__ import bugs,chunk,Bug,SimpleWorker,run_worker,computer,compute'))

print('4 processs, 25 cycles: ', timeit.timeit('compute(bugs, nb_process=4, cycles=25)', number=10, setup='from __main__ import bugs,chunk,Bug,SimpleWorker,run_worker,computer,compute'))
print('1 processs, 25 cycles: ', timeit.timeit('compute(bugs, nb_process=1, cycles=25)', number=10, setup='from __main__ import bugs,chunk,Bug,SimpleWorker,run_worker,computer,compute'))

