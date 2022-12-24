# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 19:25:03 2022

@author: xavid
"""

# Import required Python libraries

import os
import sys
import numpy as np
import scipy
from scipy import *
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Import required functions

#from feasible_graph import *

def linear_programming(x, A, b, E):
    
    # x is an array of variables of right hand side of objective function 
    obj = x
    
    # Inequality constarints left hand side
    lhs_inequality = A

    # Inequality constarints left hand side
    rhs_inequality =  b


    # Bounds
    bound = E

    # Optimization problem solution

    # Linprog with revised simplex method
    opt_rs = scipy.optimize.linprog(c=obj, A_ub=lhs_inequality, b_ub=rhs_inequality,
                                    bounds=bound,
                                    method="revised simplex")

    
    # Linprog with simplex method
    opt_s = scipy.optimize.linprog(c=obj, A_ub=lhs_inequality, b_ub=rhs_inequality,
                                   bounds=bound,
                                   method="simplex")

    # Linprog with interior point method
    opt_ip = scipy.optimize.linprog(c=obj, A_ub=lhs_inequality, b_ub=rhs_inequality,
                                    bounds=bound,
                                    method="interior-point")


    return opt_rs, opt_s, opt_ip


# maximize    z = 5X1 + 5X2 + 3Y + 1.5K
# subjet to   35X1 + 0X2 + 2Y + 1K <= 100   (diners – en €)
#             5X1 + 5X2 + 1Y + 1K <= 25     (espai al cotxe - en dm3)
#             10X1 + 10X2 + 7Y + 3K <= 60   (temps de muntar el pessebre - en minuts)
#             X1 <= 5
#             X2 <= 10 (espai cistella – en dm3)
#             Y <= 20
#             K <= 8
#             X1 >= 0
#             X2 >= 0
#             Y >= 0
#             K >= 0


# minimize    -z = -5X1 - 5X2 - 3Y - 1.5K
# subjet to   35X1 + 0X2 + 2Y + 1K <= 100   (diners – en €)
#             5X1 + 5X2 + 1Y + 1K <= 25     (espai al cotxe - en dm3)
#             10X1 + 10X2 + 7Y + 3K <= 60   (temps de muntar el pessebre - en minuts)
#             X1 <= 5
#             X2 <= 10 (espai cistella – en dm3)
#             Y <= 20
#             K <= 8
#             X1 >= 0
#             X2 >= 0
#             Y >= 0
#             K >= 0



# simplex example

objective_func = [-5, -5, -3, -1.5] # Objective function right side - minimize problem 

ineq_constraints_lhs = [[35,  0, 2, 1],  # Inequality constraint 1 left side
                        [5 ,  5, 1, 1],  # Inequality constraint left side
                        [10, 10, 7, 3]]  # Inequality constraint left side

ineq_constraints_rhs = [100,  # Inequality constraint 1 right side
                        25,  # Inequality constraint 2 right side
                        60]   # Inequality constraint 3 right side

eq_constraints_lhs = [] # Equality constraint 1 left side
eq_constraints_rhs = [] 


bounds = [(0, 5),   # Bounds of X1
          (0, 10),   # Bounds of X2
          (0, 20),   # Bounds of Y
          (0, 8)]  # Bounds of K


# Find the solution for the optimization problem
opt_revised_simplex, opt_simplex, opt_interior_point = linear_programming(objective_func, ineq_constraints_lhs, 
                                                       ineq_constraints_rhs,
                                                       bounds)

print(opt_revised_simplex)

print(opt_simplex)

print(opt_interior_point)