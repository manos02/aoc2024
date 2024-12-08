from collections import defaultdict

file = open('input.txt', 'r')
lines = file.readlines()

f = defaultdict(list)
a = []
ant = set()

lines = [l.strip() for l in lines]


for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] != '.':
            f[lines[r][c]].append((r, c))

vals = list(f.values())

count = 0
for k, v in f.items():    
    for i in range(len(v)-1):
        for j in range(i+1, len(v)):
            y = v[j][1] - v[i][1] # 0 x, 1 y
            x = v[j][0] - v[i][0]

            p1 = (v[i][0], v[i][1])
            p2 = (v[j][0], v[j][1])
            
            while True:
                p1 = (p1[0] + x, p1[1] +  y)
        
                if p1[0] >= 0 and p1[0] < len(lines[0]) and p1[1] >= 0 and  p1[1] < len(lines):
                    ant.add(p1)                    
                else:
                    break
                
            while True:
            
                p2 = (p2[0] - x, p2[1] - y)
                if p2[0] >= 0 and p2[0] < len(lines[0]) and p2[1] >= 0 and  p2[1] < len(lines):
                    ant.add(p2)
                else:
                    break

print(len(ant))
