#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import math as m

ramp = np.array([[0,0],[1/m.sqrt(2),1/m.sqrt(2)]])
base = np.array([[0,0],[1/m.sqrt(2),0]])
height = np.array([[1/m.sqrt(2),0],[1/m.sqrt(2),1/m.sqrt(2)]])


boxSides = np.array([[1/m.sqrt(2)/3,1/m.sqrt(2)/3],[1/m.sqrt(2)/3-1/m.sqrt(2)/3*m.sin(m.pi/4),1/m.sqrt(2)/3+1/m.sqrt(2)/3*m.cos(m.pi/4)]])
boxSides2 = np.array([[2/m.sqrt(2)/3,2/m.sqrt(2)/3],[2/m.sqrt(2)/3-1/m.sqrt(2)/3*m.sin(m.pi/4),2/m.sqrt(2)/3+1/m.sqrt(2)/3*m.cos(m.pi/4)]])
boxTop = np.array([[1/m.sqrt(2)/3-1/m.sqrt(2)/3*m.sin(m.pi/4),1/m.sqrt(2)/3+1/m.sqrt(2)/3*m.cos(m.pi/4)],[2/m.sqrt(2)/3-1/m.sqrt(2)/3*m.sin(m.pi/4),2/m.sqrt(2)/3+1/m.sqrt(2)/3*m.cos(m.pi/4)]])

gravity = np.array([[1/m.sqrt(2)/3+1/m.sqrt(2)/6-1/m.sqrt(2)/6*m.sin(m.pi/4),1/m.sqrt(2)/3+1/m.sqrt(2)/6+1/m.sqrt(2)/6*m.cos(m.pi/4)],[0,-1/m.sqrt(2)/3]])
normal = np.array([[1/m.sqrt(2)/3+1/m.sqrt(2)/6,1/m.sqrt(2)/3+1/m.sqrt(2)/6],[-1/m.sqrt(2)/3*m.sin(m.pi/4)-0.02,1/m.sqrt(2)/3*m.cos(m.pi/4)+0.02]])


fig = plt.figure()
ax = fig.add_subplot(1,1,1, axisbg='w')
ax.plot(ramp[:,0],ramp[:,1],linewidth=2,color='k',)
ax.plot(base[:,0],base[:,1],linewidth=2,color='k')
ax.plot(height[:,0],height[:,1],linewidth=2,color='k')
ax.plot(boxSides[:,0],boxSides[:,1],linewidth=2,color='k')
ax.plot(boxSides2[:,0],boxSides2[:,1],linewidth=2,color='k')
ax.plot(boxTop[:,0],boxTop[:,1],linewidth=2,color='k')
ax.arrow(gravity[0,0],gravity[0,1],gravity[1,0],gravity[1,1],linewidth=2,color='k')
ax.arrow(normal[0,0],normal[0,1],normal[1,0],normal[1,1],linewidth=2,color='k')
ax.text(0.2,0.3,r'$F_g$',fontsize=25)
ax.text(0.225,0.5,r'$F_n$',fontsize=25)
ax.text(0.075,0.025,r'$\theta$',fontsize=25)
ax.set_aspect('equal')
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
fig.savefig('BoxRampFBDNoFriction.pdf')
fig.show()

