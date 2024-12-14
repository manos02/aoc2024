from collections import defaultdict
import math

import sympy as sp
from sympy.solvers import solve
from sympy.abc import x, y, z


file = open('input.txt', 'r')
s = file.readlines()

s = [l.strip() for l in s if l != "\n"]

total = 0
for i in range(0, len(s)-1, 3):
    a = s[i].split(":")[1].strip()
    b = s[i+1].split(":")[1].strip()
    prize = s[i+2].split(":")[1].strip()
    
    a  = a .split()
    b = b.split()
    prize = prize.split()
    
    ax = int(a[0].split(",")[0].split("+")[1])
    ay = int(a[1].split(",")[0].split("+")[1])
    bx = int(b[0].split(",")[0].split("+")[1])
    by = int(b[1].split(",")[0].split("+")[1])
    px = int(prize[0].split("=")[1][:-1])
    py = int(prize[1].split("=")[1])

    px += 10000000000000
    py += 10000000000000

    
    eq1= sp.Eq(ax*x + bx*y, px) 
    eq2 = sp.Eq(ay*x + by*y, py)
    res = solve([eq1,eq2],set=set)
    
    for r in res[1]:
        a,b = r
        if a % 1 == 0 and b % 1 == 0:
            total += (a*3 + b*1)
            
        
print(total)