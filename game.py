import numpy as np
import pylab

def initialise(x,y):
  previous=np.zeros(x*x,dtype='i')
  current=np.zeros(x*x,dtype='i')
  samp=np.random.randint(0,x*x,size=int((x*x)/2))
  previous[samp]=1
  return previous.reshape(x,x),current.reshape(x,x)


def neighbours(x,y):
  s=0
  for x in [i-1, i, i+1]:
    for y in [j-1, j, j+1]:
      if(x == i and y == j):
          continue
      if(x != self.N and y != self.N):
          s += self.old_grid[x][y]
      elif(x == self.N and y != self.N):
          s += self.old_grid[0][y]
      elif(x != self.N and y == self.N):
          s += self.old_grid[x][0]
      else:
          s += self.old_grid[0][0]
  return s;

def play():
  





