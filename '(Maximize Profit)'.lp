\* Source Pyomo model name='(Maximize Profit)' *\

max 
x5:
+5 x1
+5 x2
+3 x3
+1.5 x4

s.t.

c_u_x6_:
+35 x1
+2 x3
+1 x4
<= 100

c_u_x7_:
+5 x1
+5 x2
+1 x3
+1 x4
<= 25

c_u_x8_:
+10 x1
+10 x2
+7 x3
+3 x4
<= 60

c_e_ONE_VAR_CONSTANT: 
ONE_VAR_CONSTANT = 1.0

bounds
   0 <= x1 <= 5
   0 <= x2 <= 10
   0 <= x3 <= 20
   0 <= x4 <= 8
end
