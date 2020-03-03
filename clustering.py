from math import *
from random import *


class Points:
  
  def __init__(self, file):
    self.filename = file
    
  def read_data(self):
    with open(self.filename) as fn:
      lines = fn.readlines()
      ps = []
      for line in lines: 
        ps.append(tuple(map(float, line.strip().split(','))))
      return ps

  def cluster(self, n=10):
    k = 3
    ps = self.read_data()
    m = sample(ps, k)
    n = 0
    while n<10:
      alloc = []  
      for i in range(len(ps)):
        p = ps[i]
        d = [None] * k
        d[0] = sqrt((p[0]-m[0][0])**2 + (p[1]-m[0][1])**2)
        d[1] = sqrt((p[0]-m[1][0])**2 + (p[1]-m[1][1])**2)
        d[2] = sqrt((p[0]-m[2][0])**2 + (p[1]-m[2][1])**2)
        min_index = d.index(min(d))
        alloc.append(min_index)
      alloc_ps = [None]*k  
      for i in range(k):
        alloc_ps[i] = []
        for j in range(len(ps)):
          if alloc[j] == i:
            alloc_ps[i].append(ps[j])
            
        x_mean = 0
        y_mean = 0
        for a in alloc_ps[i]:
          l = len(alloc_ps[i]) 
          x_mean = x_mean+(a[0])/l
          y_mean = y_mean+(a[1])/l
        new_mean = (x_mean,y_mean)
        m[i] = new_mean
      n=n+1
            
    for i in range(k):
      alloc_ps=[p for j, p in enumerate(ps) if alloc[j] == i]
      print("Cluster " + str(i) + " is centred at " + str(m[i]) + " and has " + str(len(alloc_ps)) + " points.")
            
points = Points('data/samples.csv')
points.cluster()