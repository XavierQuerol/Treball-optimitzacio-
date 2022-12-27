# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 23:09:25 2022

@author: xavid
"""

from linear_programming import linear_programming

objective_func = [-3, -1.5] # Objective function right side - minimize problem 

ineq_constraints_lhs = [[2, 1],  # Inequality constraint 1 left side
                        [1, 1],  # Inequality constraint left side
                        [7, 3]]  # Inequality constraint left side

ineq_constraints_rhs = [100,  # Inequality constraint 1 right side
                        25,  # Inequality constraint 2 right side
                        60]   # Inequality constraint 3 right side

eq_constraints_lhs = [] # Equality constraint 1 left side
eq_constraints_rhs = [] 


bounds = [(0, 20),   # Bounds of Y
          (0, 8)]  # Bounds of K


# Find the solution for the optimization problem
opt_revised_simplex, opt_simplex, opt_interior_point = linear_programming(objective_func, ineq_constraints_lhs, 
                                                       ineq_constraints_rhs,
                                                       bounds)

print(opt_revised_simplex)

print(opt_simplex)

print(opt_interior_point)