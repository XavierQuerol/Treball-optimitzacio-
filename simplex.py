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

from feasible_graph import *

def linear_programming(x, A, b, C, d, E):
    
    # x is an array of variables of right hand side of objective function 
    obj = x
    
    # Inequality constarints left hand side
    lhs_inequality = A

    # Inequality constarints left hand side
    rhs_inequality =  b

    # Equality constarints left hand side
    lhs_equality = C

    # Inequality constarints left hand side
    rhs_equality = d       

    # Bounds
    bound = E

    # Optimization problem solution

    # Linprog with revised simplex method
    opt_rs = scipy.optimize.linprog(c=obj, A_ub=lhs_inequality, b_ub=rhs_inequality,
                                    A_eq=lhs_equality, b_eq=rhs_equality, bounds=bound,
                                    method="revised simplex")

    
    # Linprog with simplex method
    opt_s = scipy.optimize.linprog(c=obj, A_ub=lhs_inequality, b_ub=rhs_inequality,
                                    A_eq=lhs_equality, b_eq=rhs_equality, bounds=bound,
                                   method="simplex")

    # Linprog with interior point method
    opt_ip = scipy.optimize.linprog(c=obj, A_ub=lhs_inequality, b_ub=rhs_inequality,
                                    A_eq=lhs_equality, b_eq=rhs_equality, bounds=bound,
                                    method="interior-point")


    return opt_rs, opt_s, opt_ip


# simplex example

objective_func = [-1, -2] # Objective function right side - minimize problem 

ineq_constraints_lhs = [[ 2,  1],  # Inequality constraint 1 left side
                        [-4,  5],  # Inequality constraint left side
                        [ 1, -2]]  # Inequality constraint left side

ineq_constraints_rhs = [20,  # Inequality constraint 1 right side
                        10,  # Inequality constraint 2 right side
                        2]   # Inequality constraint 3 right side

eq_constraints_lhs = [[-1, 5]]  # Equality constraint 1 left side
eq_constraints_rhs = [15]       # Equality constraint right side

bounds = [(0, float("inf")),  # Bounds of x
          (0, float("inf"))]  # Bounds of y


# Find the solution for the optimization problem
opt_revised_simplex, opt_simplex, opt_interior_point = linear_programming(objective_func, ineq_constraints_lhs, 
                                                       ineq_constraints_rhs, eq_constraints_lhs, eq_constraints_rhs,
                                                       bounds)