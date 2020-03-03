from math import *
from random import *
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt

class Points1:
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
      alloc_ps_i =alloc_ps[i]
      print("Cluster " + str(i) + " is centred at " + str(m[i]) + " and has " + str(len(alloc_ps_i)) + " points.")

class Points2:
  def __init__(self, file):
    self.filename = file
  def read_data2(self):
    with open(self.filename) as fn:
        ps = np.loadtxt(fn,delimiter=",",skiprows=0) 
    return ps
  def cluster2(self, n=10):
    k = 3
    ps = self.read_data2()
    rand_arr = np.arange(ps.shape[0])
    np.random.shuffle(rand_arr)
    m = ps[rand_arr[0:k]]    
    n = 0
    num = [None]*k
    while n<10:     
      d = np.zeros([len(ps),k])
      for i in range(k):
        d[:,i] = ((ps[:,0]-m[i,0])**2+ (ps[:,1]-m[i,1])**2 )**0.5
      alloc = np.argmin(d, axis=1)
      
      for i in range(k):
        itemindex = np.argwhere(alloc == i).squeeze() 
        ps_i = ps[itemindex,:]
        m[i] = ps_i.mean(axis=0)
        num[i] = ps_i.shape[0] 
      n=n+1
    
    for i in range(3):
      print("Cluster " + str(i) + " is centred at " + str(m[i]) + " and has " + str(num[i]) + " points.") 




k_list = np.arange(100, 10000, 330) 
t = np.zeros([len(k_list),2])
i = 0
for k in k_list:
    f = np.random.random((k, 2)) 
    np.savetxt('new_sample.csv', f, delimiter=',')
    points = Points1('new_sample.csv')
    tic = timer()
    points.cluster()
    toc = timer()
    t[i,0] = toc - tic
    
    points = Points2('new_sample.csv')
    tic = timer()
    points.cluster2()
    toc = timer()
    t[i,1] = toc - tic
    i = i+1

X = k_list 
C,S=t[:,0],t[:,1]
plt.plot(X,C,marker ='.' ,label = 'without numpy')
plt.plot(X,S,marker ='.',label = 'with numpy')
plt.xlabel('number of points')
plt.ylabel('time')
plt.title(' Time for clustering algorithm')
plt.legend()
plt.show()
plt.savefig('performance.png')
