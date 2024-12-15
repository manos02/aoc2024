

f = open("input.txt", 'r')
s = f.read().strip()

w = [list(r) for r in s.split("\n")]

g = []
moves = []

i = 0
while True:
    if  not w[i]:
        break
    
    g.append(w[i])
    i+=1

for j in range(i+1, len(w)):
    for elem in w[j]:
        moves.append(elem)

directions = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)} # up, right, down, left

R = len(g)
C = len(g[0])

for r in range(R):
    for c in range(C):
        if g[r][c] == '@':
            sr = r
            sc = c
            break

pos = (sr, sc)

for move in moves:
    nr = pos[0] + directions[move][0]
    nc = pos[1] + directions[move][1]

    if g[nr][nc] == '#':
        continue
    
    elif g[nr][nc] == '.':
        g[pos[0]][pos[1]] = '.'
        g[nr][nc] = '@'
        pos = (nr, nc)

    else: # found O
        
        tr = nr
        tc = nc
        while True:
            tr += directions[move][0]
            tc += directions[move][1]

            if g[tr][tc] == '#':
                break
        
            if g[tr][tc] == '.':
                g[tr][tc] = 'O'
                g[nr][nc] = '@'
                g[pos[0]][pos[1]] = '.'
                pos = (nr, nc)
                break

total = 0

for i in range(R):
    for j in range(C):
        if g[i][j] == 'O':
            total += (i*100 + j)

print(total)