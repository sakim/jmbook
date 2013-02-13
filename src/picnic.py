# -*- coding: UTF-8 -*-
def solve(n, m):
  paired = [False] * n
  friends = [[False for x in xrange(n)] for x in xrange(n)]
  for i in range(0, len(m), 2):
    l, r = (m[i], m[i+1]) if m[i] < m[i+1] else (m[i+1], m[i])
    friends[l][r] = True

  return pairing(n, 0, paired, friends)

def pairing(n, begin, paired, friends):
  finished = True
  for i in range(n):
    if not paired[i]:
      finished = False
      break

  if finished:
    return 1

  counter = 0

  for i in range(begin, n):
    for j in range(i, n):
      if not paired[i] and not paired[j] and friends[i][j]:
        paired[i] = paired[j] = True
        counter += pairing(n, i, paired, friends)
        paired[i] = paired[j] = False

  return counter

if __name__ == '__main__':
  C = int(raw_input())
  for _ in xrange(C):
    n, m = map(int, raw_input().split())
    p = map(int, raw_input().split())
    print solve(n, p)