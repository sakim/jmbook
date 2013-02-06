# -*- coding: UTF-8 -*-
# 1장 록 페스티벌
# http://algospot.com/judge/problem/read/FESTIVAL

def calculate(cost_list, min_teams):
  sums = []

  for i in range(len(cost_list)):
    sums.append(cost_list[i] if i == 0 else sums[i-1] + cost_list[i])

  min = sums[len(cost_list)-1]

  for idx in range(min_teams-1, len(sums)):
    for teams in range(min_teams-1, idx+1):
      if idx == teams:
        average = sums[idx]/float(teams+1)
      else:
        average = (sums[idx]-sums[idx-teams-1])/float(teams+1)
      min = average if average < min else min

  return min

def prompt():
  numOfCases = int(raw_input())
  for _ in range(numOfCases):
    input = raw_input()
    days_reserved = input.split(' ')
    numOfDays = days_reserved[0]
    numOfReserved = int(days_reserved[1])
    input = raw_input()
    costs = map(int, input.split(' '))

    print '%.10lf' % calculate(costs, numOfReserved)

if __name__ == '__main__':
  prompt()
