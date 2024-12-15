f = open("input.txt", 'r')
s = f.read().strip()

w = [list(r) for r in s.split("\n")]

g2 = []
moves = []

i = 0
while True:
    if  not w[i]:
        break
    
    g2.append(w[i])
    i+=1

for j in range(i+1, len(w)):
    for elem in w[j]:
        moves.append(elem)

directions = {'^':(-1,0), '>':(0,1), 'v':(1,0), '<':(0,-1)} # up, right, down, left

R2 = len(g2)
C2 = len(g2[0])

g = []
def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

for i in range(R2):
    for j in range(C2):
        if g2[i][j] == '#':
            g.append('#')
            g.append('#')
        elif g2[i][j] == '.':
            g.append('.')
            g.append('.')
        elif g2[i][j] == '@':
            g.append('@')
            g.append('.')
        elif g2[i][j] == 'O':
            g.append('[')
            g.append(']')

g = to_matrix(g, C2*2)

R = len(g)
C = len(g[0])

for r in range(R):
    for c in range(C):
        if g[r][c] == '@':
            sr = r
            sc = c
            break

pos = (sr, sc)


def check_move(r, c, dir): # row direction
    if g[r][c] == '.':
        return True
    elif g[r][c] == '#':
        return False

    if g[r][c] == ']':
        STORE.append((r, c, ']'))
        STORE.append((r, c-1, '['))
        return check_move(r+dir, c-1, dir) and check_move(r+dir, c, dir)

    elif g[r][c] == '[':
        STORE.append((r, c, '['))
        STORE.append((r, c+1, ']'))
        return check_move(r+dir, c+1, dir) and check_move(r+dir, c, dir)
    

for move in moves:


    nr = pos[0] + directions[move][0]
    nc = pos[1] + directions[move][1]

    if g[nr][nc] == '#':
        continue
    
    elif g[nr][nc] == '.':

        g[pos[0]][pos[1]] = '.'
        g[nr][nc] = '@'
        pos = (nr, nc)

    elif (g[nr][nc] == '[' or g[nr][nc] == ']') and (move == '<' or move == '>'): # found O
        
        tr = nr + directions[move][0]
        tc = nc + directions[move][1]

        while True:
            tr += directions[move][0]
            tc += directions[move][1]

            if g[tr][tc] == '#':
                break
        
            if g[tr][tc] == '.':

                while True:
                    g[tr][tc] = g[tr-directions[move][0]][tc-directions[move][1]]

                    if  g[tr][tc] == '@':
                        g[tr-directions[move][0]][tc-directions[move][1]] = '.'
                        pos = (tr, tc)
                        break
                    
                    tr -= directions[move][0]
                    tc -= directions[move][1]
                break

    elif (g[nr][nc] == '[' or g[nr][nc] == ']') and (move == '^' or move == 'v'): # found O
        

        STORE = []
        
        if check_move(nr, nc, directions[move][0]):    
            

            new = []
            for r, c, symbol in STORE:
                g[r+directions[move][0]][c] = symbol
                new.append((r+directions[move][0], c))
            
            for r, c, symbol in STORE:
                if (r,c) not in new:
                    g[r][c] = '.'

            g[nr][nc] = '@'
            g[pos[0]][pos[1]] = '.'
            pos = (nr, nc)
        
        
total = 0

for i in range(R):
    for j in range(C):
        if g[i][j] == '[':
            total += (i*100 + j)

print(total)