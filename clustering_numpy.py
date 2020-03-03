from math import *
from random import *
import numpy as np
from argparse import ArgumentParser


class Points2:
  def __init__(self, file):
    self.filename = file
  def read_data(self):
    with open(self.filename) as fn:
        ps = np.loadtxt(fn,delimiter=",",skiprows=0) 
    return ps
  def cluster(self, n=10):
    k = 3
    ps = self.read_data()
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
      
def process():          
  parser = ArgumentParser(
    description='Cluster points into 3 classes')
  parser.add_argument('data')
  parser.add_argument('--iter', help='iteration time for clustering')
  args = parser.parse_args()
    
  points = Points2(args.data)
  if args.iter:
    points.cluster(args.iter)
  else:
    points.cluster()

if __name__ == "__main__":
  process()
