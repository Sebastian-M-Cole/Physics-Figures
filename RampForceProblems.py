#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import math as m

class Ramp(object):
    def __init__(self, height, angle):
        self.height = height
        self.angle = angle*m.pi/180
        
        self.ramp = np.zeros((4,2))
        self.ramp[1,0] = height/m.tan(self.angle)
        self.ramp[1,1] = 0
        self.ramp[2,0] = self.ramp[1,0]
        self.ramp[2,1] = height
        self.ramp[3,:] = self.ramp[0,:]
           
    def ConstructRamp(self,ax):
        ax.plot(self.ramp[:,0],self.ramp[:,1],linewidth=2,color='k')

class Box(object):
    def __init__(self, length, width, mass, friction=False):
        self.length = length
        self.width = width
        
        self.box = np.zeros((5,2))
        self.box[1,0] = length
        self.box[2,0] = self.box[1,0]
        self.box[2,1] = width
        self.box[3,1] = self.box[2,1]
    
        self.mass = mass
        self.friction = friction

    def ConstructBox(self,ax):
        ax.plot(self.box[:,0],self.box[:,1],linewidth=2,color='k')

    def RotateBox(self,angle):
        rotMatrix = np.array([[m.cos(angle), -m.sin(angle)],[m.sin(angle), m.cos(angle)]])
        for i in range(np.shape(self.box)[0]):
            self.box[i,:] = np.transpose(np.dot(rotMatrix,np.transpose(self.box[i,:])))

    def ShiftBox(self,height,angle):
        x_shift = height/m.tan(angle)/3
        y_shift = height/3

        for i in range(np.shape(self.box)[0]):
            self.box[i,0] = self.box[i,0]+x_shift
            self.box[i,1] = self.box[i,1]+y_shift


class BoxOnRamp(Box,Ramp):
    def __init__(self, height, angle, mass, friction=False):
        Box.__init__(self,height/3,height/3,mass)
        Ramp.__init__(self,height,angle)
        self.RotateBox(self.angle)
        self.ShiftBox(self.height,self.angle)
        self.ax, self.fig = self.BuildFigure()

    def BuildFigure(self):
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1, facecolor='w')
        ax.set_aspect('equal')
        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        return ax,fig

    def ConstructBoxOnRamp(self):
        self.ConstructRamp(self.ax)
        self.ConstructBox(self.ax)

    def ConstructBoxFBD(self):
        g = 9.8
        mu_k = 0.1
        F_g = -self.mass*g
        if self.friction is False:
            F_nx = F_g*m.sin(self.angle)
            F_ny = -F_g*m.cos(self.angle)
        else:
            f = -F_g*m.cos(self.angle)*mu_k
            f_x = f*m.cos(self.angle)
            f_y = f*m.sin(self.angle)
            F_nx = F_g*m.sin(self.angle)
