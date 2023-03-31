import numpy as np
from field.func import *

st = {0,1}
add = {(0,0):0,
       (0,1):1,
       (1,0):1,
       (1,1):0}

mult = {(0,0):0,
       (0,1):0,
       (1,0):0,
       (1,1):1}

z2 = FiniteAlg(st,add,mult)



#print("tour group challenge")

#for ord in range(30):
#    st = set(range(ord))
#    add = {}
#    mult = {}
#    for i in st:
#        for j in st:
#            add[(i,j)] = (i+j)%ord
#            mult[(i,j)] = (i*j)%ord
#    z = FiniteAlg(st,add,mult)
#    if(z.alg == "field"):
#        print(ord)

#x = z2(0)
#y = z2(1)
#print("x+y = ",x+y)



ord = 7

st = set(range(ord))
add = {}
mult = {}
for i in st:
    for j in st:
        add[(i,j)] = (i+j)%ord
        mult[(i,j)] = (i*j)%ord
z = FiniteAlg(st,add,mult)
print(z.alg)
x = z(3)
y = z(0)
z = y*y
print(z)