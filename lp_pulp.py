# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 19:37:55 2022

@author: xavid
"""
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable


model = LpProblem(name="Pessebre", sense=LpMaximize) #model buit, sense valors

# Initializing the decision variables

x1 = LpVariable(name="x1", lowBound=0, upBound = 5)  
x2 = LpVariable(name="x2", lowBound=0, upBound = 10) 
y = LpVariable(name="y", lowBound=0, upBound = 20) 
k = LpVariable(name="k", lowBound=0, upBound = 8, cat="Integer")

# variables can be defines without category as well as below.
# lower bound for -ve infinity (negatiu) is given by 0 and upper can be ommitted due to being +infinity

# Adding the constraints to the model

model += (35 * x1 + 0 * x2 + 2 * y + 1 * k <= 100) 
model += (5 * x1 + 5 * x2 + 1 * y + 1 * k <= 25) 
model += (10 * x1 + 10 * x2 + 7 * y + 3 * k <= 60) 


# Adding the objective function to the model

object_func = 5 * x1 + 5 * x2 + 3 * y + 1.5 * k
model += object_func


# Solve the problem
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")  

#Output: status: 1, Optimal 
#The function value() and the corresponding method .value() return the actual values of the attributes:

print(f"objective: {model.objective.value()}")

# Output: objective
# Printing the values of the variables: 

for var in model.variables():
    print(f"{var.name}: {var.value()}")


for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")

# Finding which solver is used
model.solver
# <pulp.apis.coin_api.PULP_CBC_CMD at 0x7f40eb4612e0> 

# Output: 

# The output informs that the solver is default CBC solver. 
# Now lets import the solver GLPK and solve the problem with this solver

from pulp import PULP_CBC_CMD
status = model.solve(solver=PULP_CBC_CMD(msg=False)) 




