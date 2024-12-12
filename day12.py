

file = open('input.txt', 'r')
s = file.read().strip()

g = [list(r) for r in s.split("\n")]

R = len(g)
C = len(g[0])



def follow(grid, row, col, symbol, region):

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # down, right, up, left

    if row >= R or row < 0 or col >= C or col < 0:
        return
    
    if grid[row][col] != symbol or (row, col) in region:
        return

    region.append((row,col))

    for d in directions:
        r = row + d[0]
        c = col + d[1]
        
        follow(grid, r, c, symbol, region)
        

    return

def find_perimeter(grid, region):
    p = 0
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # down, right, up, left
    for r, c in region:
        for d in directions:
            nr = r + d[0]
            nc = c + d[1]

            if (nr, nc) in region:  
                continue
            p += 1
    return p

seen = []
count = 0

for row in range(R):
    for col in range(C):
        if (row, col) not in seen:
            region = []
            follow(g, row, col, g[row][col], region)
            seen.extend(region)
            p = find_perimeter(g, region)
            count += (p*len(region))
    
print(count)