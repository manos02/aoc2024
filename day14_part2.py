from collections import defaultdict

f = open("input.txt", 'r')
s = f.readlines()

R = 103
C = 101

positions = defaultdict(int)

init_pos = []
grid = [['0'] * C for _ in range(R)]


for l in s:
    l = l.split("\n")[0]
    p, v = l.split()
    p = p.split("=")[1].split(",")
    v = v.split("=")[1].split(",")
    
    pos = [int(p[0]), int(p[1])]
    vel = [int(v[0]), int(v[1])]

    
    grid[pos[1]][pos[0]] = '*'

    init_pos.append([pos, vel])

    positions[(pos[0], pos[1])] += 1



for second in range(20000):
    for r in range(len(init_pos)):
        
        pos = init_pos[r][0]
        vel = init_pos[r][1]

        positions[(pos[0], pos[1])] -= 1
        
        if positions[(pos[0], pos[1])] <= 0:
            grid[pos[1]][pos[0]] = '0'
        
        init_pos[r][0][0] += vel[0]
        init_pos[r][0][1] += vel[1]
        
        init_pos[r][0][0] %= C
        init_pos[r][0][1] %= R

        positions[(init_pos[r][0][0], init_pos[r][0][1])] += 1

        grid[init_pos[r][0][1]][init_pos[r][0][0]] = '*'    
    
    flag = False
    for i in range(R):
        for j in range(C-19):
            if all(e == '*' for e in grid[i][j:j+20]):  
                flag = True
            
    if flag:
        print('\n'.join(map(''.join, grid)))
        print("second: ", second)
        break  
