# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 23:24:32 2022

@author: xavid
"""

import os
import sys

import numpy as np
import matplotlib.pyplot as plt

# plot the feasible region
d = np.linspace(0,600)
x,y = np.meshgrid(d,d)

ineq_1 = 2*x + 1*y <= 100
ineq_2 = 1*x+1*y <= 25
ineq_3 = 7*x + 3*y <= 60
ineq_4 = y <= 20 + 0*x
ineq_5 = x <= 8 + 0*y

#plt.imshow( (ineq_1 & ineq_2 & ineq_3 & ineq_4 & ineq_5).astype(int) , 
                #extent=(x.min(),x.max(),y.min(),y.max()),origin="lower", cmap="Greys", alpha = 0.3);

# plot the lines defining the constraints
x = np.linspace(-600, 600, 2000)
y =  np.linspace(-600, 600, 2000)
y1 = 100 - 2*x
y2 = 25 - 1*x
y3 = (60 - 7*x) / 3
y4 = 20 + 0*x
x1 = 8 + 0*y

# Make plot
plt.plot(x, y1, label=r'2*Y + 1*K <= 100')
plt.plot(x, y2, label=r'1*Y +  1*K <= 25')
plt.plot(x, y3,label=r'7*Y + 3*K <= 60')
plt.plot(x, y4,label=r'K <= 20')
plt.plot(x1, y,label=r'Y <= 8')

plt.xlim(0,100)
plt.ylim(0,100)
plt.legend(bbox_to_anchor=(0.35, 0.95), loc=2, borderaxespad=0.)
plt.xlabel(r'$Neu$')
plt.ylabel(r'$Figures$')

plt.savefig("figure2var.jpg", dpi = 2000)