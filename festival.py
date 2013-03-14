# -*- coding: UTF-8 -*-
# 1장 록 페스티벌
# http://algospot.com/judge/problem/read/FESTIVAL


# method (1): 7000ms
def solve(D, L):
    sums = []

    for i in range(len(D)):
        sums.append(D[i] if i == 0 else sums[i - 1] + D[i])

    minimum = sums[len(D) - 1]

    for idx in xrange(L - 1, len(sums)):
        for teams in xrange(L - 1, idx + 1):
            if idx == teams:
                average = sums[idx] / float(teams + 1)
            else:
                average = (sums[idx] - sums[idx - teams - 1]) / float(teams + 1)
            minimum = average if average < minimum else minimum

    return minimum

if __name__ == '__main__':
    C = int(raw_input())
    for _ in xrange(C):
        N, L = map(int, raw_input().split())
        D = map(int, raw_input().split())
        print '%.10lf' % solve(D, L)
