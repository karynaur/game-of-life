import numpy as np
import pylab
import glob
import moviepy.editor as mpy

import os
def initialise(x):
  previous=np.zeros(x*x,dtype='i')
  current=np.zeros(x*x,dtype='i')
  samp=np.random.randint(0,x*x,size=int((x*x)/2))
  previous[samp]=1
  return previous.reshape(x,x),current.reshape(x,x)


def neighbours(i,j,old):
  s=0
  for x in [i-1, i, i+1]:
    for y in [j-1, j, j+1]:
      if(x == i and y == j):
          continue
      if(x != 100 and y != 100):
          s += old[x][y]
      elif(x == 100 and y != 100):
          s += old[0][y]
      elif(x != 100 and y == 100):
          s += old[x][0]
      else:
          s += old[0][0]
  return s;

def play(): 
  old,new=initialise(100)
  gen=500
  pylab.pcolormesh(old)
  pylab.colorbar()
  pylab.savefig("gen-0.png")
  t=1

  while(t<=gen):
    if(t%10==0):print(t)
    for i in range(100):
      for j in range(100):
         live=neighbours(i,j,old)
         if(old[i][j] == 1 and live < 2):
            new[i][j] = 0 
         elif(old[i][j] == 1 and (live == 2 or live == 3)):
            new[i][j] = 1
         elif(old[i][j] == 1 and live > 3):
            new[i][j] = 0 
         elif(old[i][j] == 0 and live == 3):
            new[i][j] = 1

    if(t%5==0):
      pylab.pcolormesh(new)
      pylab.savefig("gen-%d.png" %t)

    old=new.copy()
    t=t+1
  gif_name=str(gen)
  fps=12
  file_list=glob.glob('*.png')
  list.sort(file_list, key=lambda x: int(x.split('.png')[0].split('-')[1]))
  clip = mpy.ImageSequenceClip(file_list[0:41],fps=fps)
  clip.write_videofile("gameoflife.mp4",fps=fps)

  del clip
  a = [os.remove(f) for f in file_list]

play()

