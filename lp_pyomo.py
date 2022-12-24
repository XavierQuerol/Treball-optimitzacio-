# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 19:30:18 2022

@author: xavid
"""

from pyomo import environ as pe
from pyomo.environ import * 



os.environ['NEOS_EMAIL'] = 'XQUEROLESO@GMAIL.COM'

# Creating Pyomo model
model = pe.ConcreteModel(name="(Maximize Profit)") 

# Defining the decision variables
model.X1 = pe.Var(bounds = (0,5), name = 'X1') 
model.X2 = pe.Var(bounds = (0,10), name = 'X2')
model.Y = pe.Var(bounds = (0,20), name = 'Y')
model.K = pe.Var(bounds = (0,8), name = 'K')

model.objective = pe.Objective(expr = 5*model.X1 + 5*model.X2 + 3*model.Y + 1.5*model.K, sense = maximize)
model.constraints = pe.ConstraintList()
model.constraints.add(35*model.X1 + 0*model.X2 + 2*model.Y + 1*model.K <= 100); # constraint-1 
model.constraints.add(5*model.X1 + 5*model.X2 + 1*model.Y + 1*model.K <= 25); # constraint-2 
model.constraints.add(10*model.X1 + 10*model.X2 + 7*model.Y + 3*model.K <= 60); # constraint-3

solver_manager = pe.SolverManagerFactory('neos')

results = solver_manager.solve(model, solver = "minto")
print(results)

results = solver_manager.solve(model, solver = "minos")
print(results)

results = solver_manager.solve(model, solver = "cbc")
print(results)

results = solver_manager.solve(model, solver = "mosek")
print(results)

print('X1 =', model.X1.value)
print('X2 =', model.X2.value)
print('Y =', model.Y.value)
print('K =', model.K.value)

# Retreiving the objective value

print('The objective value is =',model.objective())

# Saving the model in a file. This will create file with model name.

model.write();

# Display the complete model as follows:

model.display()

model.write();