file = open('input2.txt', 'r')
lines = file.read().strip().split()

d = 0 

for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == "^":
            sr = r
            sc = c
            break
            

count = 0
c1 = 0

for row in range(len(lines)):
    for col in range(len(lines[0])):
        r, c = sr, sc
        visited = set()
        d = 0
        while True:
            if (r, c, d) in visited:
                c1 += 1
                break
            visited.add((r, c, d))
            if d == 0:
                nr = r - 1
                nc = c
            elif d == 1:
                nc = c+1
                nr = r
            elif d == 2:
                nr = r + 1
                nc = c
            else:
                nc = c-1
                nr = r
 
            
            if not (0<=nr<len(lines) and  0<=nc<len(lines[0])):
                break
            if lines[nr][nc] == '#' or nr==row and nc==col:
                d = (d+1) % 4
            else:
                r = nr
                c = nc


print(c1)
