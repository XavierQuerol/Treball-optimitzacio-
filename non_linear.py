# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 19:36:11 2022

@author: xavid
"""

from scipy.optimize import minimize
from numdifftools import Jacobian
import numpy as np
import time


# Example Problem 1 : Solve the following NLP using Scipy minimizer

#  min      l1^2 + l2^2(?)
#  s.t.     -l1^2 - l2^2 + 4800(mida total hipotètica pessebre) ≤ 0
#           2*l2^2 - l1^2 ≤ 0
#           l1 - 71 ≤ 0
#           l2 - 43 ≤ 0 
#           -l1 ≤ 0
#           -l2 ≤ 0
#                   
#  var      l1, l2

# Write objective objction
obj = lambda f: f[0]**2 #+ f[1]**2

# Provide constraints

cons = (
        {'type': 'ineq', 'fun': lambda f: f[0]**2 + f[1]**2 -4800.}, 
        {'type': 'ineq', 'fun': lambda f: f[0]**2-2*f[1]**2}, 
        {'type': 'ineq', 'fun': lambda f: f[0]}, 
        {'type': 'ineq', 'fun': lambda f: -f[0] + 71.}, 
        {'type': 'ineq', 'fun': lambda f: f[1]}, 
        {'type': 'ineq', 'fun': lambda f: -f[1] + 66.}
        )

# Define bounds
bnds = ((None, None), (None, None))
bnds = ((None, None), )*2

# initial guess
x0 = (10,10) # feasible initian point
# x0 = (0,0) # non-feasible initian point

# Method SLSQP uses Sequential Least SQuaresult Programming to minimize a objction 
# of several variables with any combination of bounds, equality and inequality constraints. 
# Please consult http://www.pyopt.org/reference/optimizers.slsqp.html for more details for SLSQP

start_time = time.time()*1000

# Find the optimal value via minimizer within provided time without jacobian

result = minimize(obj, x0, method='SLSQP', bounds=bnds, constraints=cons)

end_time = time.time()*1000

# Print the resultults

print(result)

# Print the value of objective func
print("optimal value p*", result.fun)

# print the value of decision variable
print("optimal variables: l1 = ", result.x[0], " l2 = ", result.x[1])

# print the time execution time
print("exec time (ms): ", end_time - start_time)


# Find the optimal value via minimizer within provided time with jacobian

# Find Jacobian
obj_Jac = lambda x: Jacobian(lambda x: obj(x))(x).ravel()

start_time = time.time()*1000

result2 = minimize(obj, x0, method='SLSQP', bounds=bnds, constraints=cons,jac=obj_Jac)

end_time = time.time()*1000

# Print the value of objective func, decision variables and execution time

print('\n',result2)
print("Jacobian: optimal value p*", result2.fun)
print("Jacobian: optimal variables: l1 = ", result2.x[0], " l2 = ", result2.x[1])
print("exec time (ms): ", end_time - start_time)


## Plot the objectice function to look at the optimal values

# Import the required packages

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Initizalize the graph plot
fun_fig = plt.figure()

# define the objectice function
objec = lambda f: f[0]**2 #+ f[1]**2

f = np.linspace(0, 100, 30)
y = np.linspace(0, 100, 30)


X, Y = np.meshgrid(f, y)

Z = objec([X,Y])

fun_fig = plt.figure()

fig = plt.axes(projection='3d')

fig.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none', alpha=.8)

plt.plot(result2.x[0], result2.x[1], result2.fun, marker="x", markersize=10, markeredgecolor="black", markerfacecolor="black")

# ax.scatter(1, 1, color='black') # scatter plot

#
fig.contour3D(X, Y, Z, 50, cmap='binary')

# Graph labels

fig.set_xlabel('x1')
fig.set_ylabel('x2')
fig.set_zlabel('objec')

# Graph window
fig.view_init(50, 135)