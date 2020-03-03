from math import *
from random import *
import numpy as np
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from clustering import cluster 
from clustering_numpy import cluster as cluster2 

k_list = np.arange(100, 10000, 330) 
t = np.zeros([len(k_list),2])
i = 0
for k in k_list:
  f = np.random.random((k, 2)) 
  np.savetxt('new_sample.csv', f, delimiter=',')
    
  with open('new_sample.csv') as fn:
    lines = fn.readlines()
    ps = []
    for line in lines: 
      ps.append(tuple(map(float, line.strip().split(','))))
    tic = timer()
    cluster(ps)
    toc = timer()
    t[i,0] = toc - tic
    
    tic = timer()
    cluster2(f)
    toc = timer()
    t[i,1] = toc - tic
    i = i+1

X = k_list 
C,S=t[:,0],t[:,1]
plt.plot(X,C,marker ='.' ,label = 'without numpy')
plt.plot(X,S,marker ='.',label = 'with numpy')
plt.xlabel('number of points')
plt.ylabel('time(s)')
plt.title(' Time for clustering algorithm')
plt.legend()
plt.savefig('performance.png')
plt.show()
