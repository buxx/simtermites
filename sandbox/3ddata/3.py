import timeit
from random import choice

grid_size = (999, 999, 99)

class Bug(object):
  def __init__(self, id):
    self.id = id
    self.trace = []
  def get_possibles_future_trace_point(self):
    point =  self.trace[0]
    possible_points = []
    
    possible_points.append((point[0]-1, point[1]+1, point[2]))
    possible_points.append((point[0],   point[1]+1, point[2]))
    possible_points.append((point[0]+1, point[1]+1, point[2]))
    possible_points.append((point[0]-1, point[1],   point[2]))
    possible_points.append((point[0]+1, point[1],   point[2]))
    possible_points.append((point[0]-1, point[1]-1, point[2]))
    possible_points.append((point[0],   point[1]-1, point[2]))
    possible_points.append((point[0]+1, point[1]-1, point[2]))
    
    possible_points_oks = []
    for possible_point in possible_points:
      ok = True
      if possible_point in self.trace:
        ok = False
      else:
        for point in possible_point:
          if point < 0:
            ok = False
        if ok:
          possible_points_oks.append(possible_point)
    
    return possible_points_oks

def get_bugs(n):
  bugs = []
  for i in range(n):
    bugs.append(Bug(i))
  return bugs

def set_bugs_3d_random_trace(bugs, trace_length = 2):
  for bug in bugs:
    while len(bug.trace) <= trace_length:
      bug.trace.append(get_bug_new_trace_point(bug))

def get_bug_new_trace_point(bug):
  if not bug.trace:
    return (choice(range(0, grid_size[0])), choice(range(0, grid_size[1])), choice(range(0, grid_size[2])))
  return get_point_near_this_point(bug.trace[len(bug.trace)-1])

def get_point_near_this_point(point):
  x = choice([-1, 0, 1])
  y = choice([-1, 0, 1])
  z = choice([-1, 0, 1])
  new_point = (point[0] + x, point[1] + y, point[2] + z)
  if (new_point[0] > 0 and new_point[0] <= grid_size[0]) and\
     (new_point[1] > 0 and new_point[1] <= grid_size[1]) and\
    (new_point[2] > 0 and new_point[2] <= grid_size[2]):
    return new_point
  return get_point_near_this_point(point)

def get_positioned_bugs(n):
  bugs = get_bugs(n)
  set_bugs_3d_random_trace(bugs)
  return bugs

def get_str_map(bugs):
  map = {}
  for bug in bugs:
    for trace_point in bug.trace:
      map[str(trace_point[0])+'.'+str(trace_point[1])+'.'+str(trace_point[2])] = bug
  return map

def get_tuple_map(bugs):
  map = {}
  for bug in bugs:
    for trace_point in bug.trace:
      map[trace_point] = bug
  return map

def get_int_map(bugs):
  map = {}
  for bug in bugs:
    for trace_point in bug.trace:
      key = trace_point[0]*100000+trace_point[1]*100+trace_point[2]
      map[key] = bug
  return map

def get_3d_map(bugs):
  map = {}
  for bug in bugs:
    for trace_point in bug.trace:
      x = trace_point[0]
      y = trace_point[1]
      z = trace_point[2]
      if x not in map:
        map[x] = {}
      if y not in map[x]:
        map[x][y] = {}
      map[x][y][z] = bug
  return map

def find_collisions_str_map(bugs, map_str):
  collisions_bugs = []
  for bug in bugs:
    for trace_point in bug.get_possibles_future_trace_point():
      #import pdb; pdb.set_trace()
      key = str(trace_point[0])+'.'+str(trace_point[1])+'.'+str(trace_point[2])
      if key in map_str:
        if map_str[key].id != bug.id:
          collisions_bugs.append(map_str[key])
  return collisions_bugs

def find_collisions_tuple_map(bugs, map):
  collisions_bugs = []
  for bug in bugs:
    for trace_point in bug.get_possibles_future_trace_point():
      if trace_point in map:
        if map[trace_point].id != bug.id:
          collisions_bugs.append(map[trace_point])
  return collisions_bugs


def find_collisions_int_map(bugs, map_str):
  collisions_bugs = []
  for bug in bugs:
    for trace_point in bug.get_possibles_future_trace_point():
      key = trace_point[0]*1000000+trace_point[1]*1000+trace_point[2]
      if key in map_str:
        if map_str[key].id != bug.id:
          collisions_bugs.append(map_str[key])
  return collisions_bugs

def find_collisions_3d_map(bugs, map):
  collisions_bugs = []
  for bug in bugs:
    for trace_point in bug.get_possibles_future_trace_point():
      x = trace_point[0]
      y = trace_point[1]
      z = trace_point[2]
      if x in map:
        if y in map[x]:
          if z in map[x][y]:
            collisions_bugs.append(map[x][y][z])
  return collisions_bugs

bugs = get_positioned_bugs(100000)
map_str = get_str_map(bugs)
map_int = get_int_map(bugs)
map_3d = get_3d_map(bugs)
map_tuple = get_tuple_map(bugs)

print('str', timeit.timeit('find_collisions_str_map(bugs, map_str)', number=10, setup='from __main__ import find_collisions_str_map, bugs, map_str'))
print('int', timeit.timeit('find_collisions_int_map(bugs, map_int)', number=10, setup='from __main__ import find_collisions_int_map, bugs, map_int'))
print('3d ', timeit.timeit('find_collisions_3d_map(bugs, map_3d)', number=10, setup='from __main__ import find_collisions_3d_map, bugs, map_3d'))
print('tup', timeit.timeit('find_collisions_tuple_map(bugs, map_tuple)', number=10, setup='from __main__ import find_collisions_tuple_map, bugs, map_tuple'))