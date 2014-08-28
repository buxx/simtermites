import timeit

def get_list(n):
  list = []
  for i in range(n):
    list.append(i)
  return list

def get_prepared_list(n):
  list = [None] * n
  for i in range(n):
    list[i] = i
  return list

print(timeit.timeit('get_list(1000000)', number=100, setup='from __main__ import get_list'))
print(timeit.timeit('get_prepared_list(1000000)', number=100, setup='from __main__ import get_prepared_list'))
