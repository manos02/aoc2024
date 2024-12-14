from collections import defaultdict
import math

import sympy as sp
from sympy.solvers import solve
from sympy.abc import x, y, z


file = open('input.txt', 'r')
s = file.readlines()

s = [l.strip() for l in s if l != "\n"]

BEST = {}

def msolve(ba, bb, prize, total, tokens, steps):

    total_tuple = tuple(total)
    if total_tuple in SEEN:
        return
    
    SEEN.add(total_tuple)

    if steps > 200:
        return

    if (prize[0], prize[1]) in BEST and tokens > BEST[(prize[0], prize[1])]:
        return

    if total[0] > prize[0] or total[1] > prize[1]:
        return


    if total[0] == prize[0] and total[1] == prize[1]:        
        if (prize[0], prize[1]) not in  BEST or tokens < BEST[(prize[0], prize[1])]:
            BEST[(prize[0], prize[1])] = tokens
            return 
    
    msolve(ba, bb, prize, [total[0]+ba[0], total[1]+ba[1]], tokens+3, steps+1)
    msolve(ba, bb, prize, [total[0]+bb[0], total[1]+bb[1]], tokens+1, steps+1)


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

    SEEN = set()
    msolve((ax, ay), (bx,by), (px, py), [0,0], 0, 0)

        
for k,v in BEST.items():
    total += v


print(total)