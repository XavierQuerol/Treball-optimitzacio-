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

#  min      4*Y^2 + K^2
#  s.t.     -2Y -K ≤ -100
#           -Y -K ≤ -25
#           -7Y -3K ≤ -60
#           -4Y^2 - K^2 + 10 ≤ 0
#           -Y^2 - K ≤ 0
#           -Y ≤ 0
#           -Y + 20 ≤ 0
#           -K ≤ 0
#           -K + 8 ≤ 0         
#  var      Y, K

# Write objective objction
obj = lambda f: 4*f[0]**2 + f[1]**2

# Provide constraints
cons = ({'type': 'ineq', 'fun': lambda f: 2*f[0] + f[1] -100.},
        {'type': 'ineq', 'fun': lambda f: f[0] + f[1] - 25.},
        {'type': 'ineq', 'fun': lambda f: 7*f[0] + 3*f[1] -60.},
        {'type': 'ineq', 'fun': lambda f: 4*f[0]**2 + f[1]**2 -10.},
        {'type': 'ineq', 'fun': lambda f: f[0]**2 + f[1]},
        {'type': 'ineq', 'fun': lambda f: f[1]},
        {'type': 'ineq', 'fun': lambda f: f[0] - 20.},
        {'type': 'ineq', 'fun': lambda f: f[1]},
        {'type': 'ineq', 'fun': lambda f: f[1] -8.}
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
print("optimal variables: x1 = ", result.x[0], " x2 = ", result.x[1])

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
print("Jacobian: optimal variables: Y = ", result2.x[0], " K = ", result2.x[1])
print("exec time (ms): ", end_time - start_time)


## Plot the objectice function to look at the optimal values

# Import the required packages

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Initizalize the graph plot
fun_fig = plt.figure()

# define the objectice function
objec = lambda f: 4*f[0]**2 + f[1]**2 

f = np.linspace(-100, 100, 30)
y = np.linspace(-100, 100, 30)


X, Y = np.meshgrid(f, y)

Z = objec([X,Y])

fun_fig = plt.figure()

fig = plt.axes(projection='3d')

fig.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none', alpha=.8)

# ax.scatter(1, 1, color='black') # scatter plot

# 
fig.contour3D(X, Y, Z, 50, cmap='binary')

# Graph labels

fig.set_xlabel('x1')
fig.set_ylabel('x2')
fig.set_zlabel('objec')

# Graph window
fig.view_init(50, 135)