from math import *
from random import *
import numpy as np
from argparse import ArgumentParser


def read_data(name):
  with open(name) as fn:
    ps = np.loadtxt(fn,delimiter=",",skiprows=0) 
  return ps

def cluster(ps, N):
  k = 3
  rand_arr = np.arange(ps.shape[0])
  np.random.shuffle(rand_arr)
  m = ps[rand_arr[0:k]]    
  n = 0
  num = [None]*k
  while n<N:     
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
      
def process():    
  parser = ArgumentParser(
    description='Cluster points into 3 classes')
  parser.add_argument('data')
  parser.add_argument('--iters',  type=int, help='iteration times for clustering',default=10)
  args = parser.parse_args()
  ps = read_data(args.data)  
  cluster(ps,args.iters)

if __name__ == "__main__":
  process()
