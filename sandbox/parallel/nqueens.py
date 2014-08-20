import os
import sys
from itertools import permutations
from multiprocessing import Process, Pipe, current_process
from multiprocessing.connection import wait

if sys.version_info < (3, 3):
  sys.stdout.write("Python 3.3 required\n")
  sys.exit(1)

def print_board(n, board):
  board_sep, board_top = '\n---\n', '+'+'-+'*n
  print(board_top)
  for l in board:
    print('|'+' |'*l+'Q|'+' |'*(n-l-1))
  print(board_top, end=board_sep)

def check_nqueens(w, n, columns, boards):
  for board in boards:
    if n == len(set(board[i]+i for i in columns)) \
         == len(set(board[i]-i for i in columns)):
      print ('%s found by %s' % (board, os.getpid()))
      w.send(board)

def nqueens(n, nb_process=2):
  columns = range(n)
  boards = list(permutations(columns))
  readers = []
  
  for i in range(nb_process):
    r, w = Pipe(duplex=False)
    readers.append(r)
    p = Process(target=check_nqueens, args=(w, n, columns, boards[i::nb_process]))
    p.start()
    w.close()
  
  while readers:
    for r in wait(readers):
      try:
        msg = r.recv()
      except EOFError:
        readers.remove(r)
      else:
        print_board(n, msg)

nqueens(4)