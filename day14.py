from collections import defaultdict

f = open("input.txt", 'r')
s = f.readlines()

R = 103
C = 101

positions = defaultdict(int)


seconds = 100

for l in s:
    l = l.split("\n")[0]
    p, v = l.split()
    p = p.split("=")[1].split(",")
    v = v.split("=")[1].split(",")
    
    pos = [int(p[0]), int(p[1])]
    vel = [int(v[0]), int(v[1])]


    pos[0] += (vel[0] * seconds) 
    pos[1] += (vel[1] * seconds) 
    pos[0] %= C
    pos[1] %= R

    positions[(pos[0], pos[1])] += 1
        

qWide = C // 2
qTall = R // 2

f, s, t, fo = 0, 0, 0, 0 


for i in range(qTall):
    for j in range(qWide):
        if (j,i) in positions:
            f += positions[(j,i)]

for i in range(qTall):
    for j in range(qWide+1, C):
        if (j,i) in positions:
            s += positions[(j,i)]

for i in range(qTall+1, R):
    for j in range(qWide):
        if (j,i) in positions:
            t += positions[(j,i)]

for i in range(qTall+1, R):
    for j in range(qWide+1, C):
        if (j, i) in positions:
            fo += positions[(j,i)]
        
print(f*s*t*fo)