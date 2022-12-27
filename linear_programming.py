# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 23:15:53 2022

@author: xavid
"""
from scipy.optimize import linprog


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
    opt_rs = linprog(c=obj, A_ub=lhs_inequality, b_ub=rhs_inequality,
                                    bounds=bound,
                                    method="revised simplex")

    
    # Linprog with simplex method
    opt_s = linprog(c=obj, A_ub=lhs_inequality, b_ub=rhs_inequality,
                                   bounds=bound,
                                   method="simplex")

    # Linprog with interior point method
    opt_ip = linprog(c=obj, A_ub=lhs_inequality, b_ub=rhs_inequality,
                                    bounds=bound,
                                    method="interior-point")


    return opt_rs, opt_s, opt_ip