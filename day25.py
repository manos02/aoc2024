f = open("input.txt", "r")
f = f.read().strip()
f = f.split("\n\n")

R = 7
C = 5

KEYS, LOCKS = [], []

def process_grid(g):

    g = [list(row) for row in grid]
    tm = []
    
    if g[0][0] == "#":
        for c in range(C):
            temp = 0
            for r in range(1, R):
                if g[r][c] == "#":
                    temp += 1

            tm.append(temp)
        LOCKS.append(tm)
    else:
        for c in range(C):
            temp = 0
            for r in range(R-1, -1, -1):
                if g[r][c] == "#":
                    temp += 1
            tm.append(temp-1)

        KEYS.append(tm)


g = [grid.split('\n') for grid in f]


for grid in g:
    process_grid(grid)
    

count = 0

for k in KEYS:
    for l in LOCKS:
        for z in range(len(k)):
            if k[z] + l[z] >= 6:
                count += 1
                break


print((len(KEYS)*len(LOCKS))-count)

