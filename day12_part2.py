

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

def find_perimeter(region):

    direction_map = {
    (1, 0): "down",
    (0, 1): "right",
    (-1, 0): "up",
    (0, -1): "left"
    }

    sq = []
    
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] # down, right, up, left
    for r, c in region:
        
        for d in directions:
            nr = r + d[0]
            nc = c + d[1]

            if (nr, nc) in region:
                continue

            sq.append((r, c, d))



    for r,c,d in sq:
        if direction_map[d] == "right" or direction_map[d] == "left":
            i = 1
            while True:
                nr = r + i
                nc = c
                if (nr, nc, d) in sq:
                    sq.remove((nr,nc, d))
                    i+=1
                else:
                    break
            i = -1
            while True:
                nr = r + i
                nc = c
                if (nr, nc, d) in sq:
                    sq.remove((nr,nc, d))
                    i-=1
                else:
                    break

        elif direction_map[d] == "down" or direction_map[d] == "up":
            i = 1
            while True:
                nr = r
                nc = c + i
                if (nr, nc, d) in sq:
                    sq.remove((nr,nc, d))
                    i+=1
                else:
                    break
            i = -1
            while True:
                nr = r
                nc = c + i
                if (nr, nc, d) in sq:
                    sq.remove((nr,nc, d))
                    i-=1
                else:
                    break
    
    return len(sq)

seen = []
count = 0

for row in range(R):
    for col in range(C):
        if (row, col) not in seen:
            region = []
            follow(g, row, col, g[row][col], region)
            seen.extend(region)
            p = find_perimeter(region)
            count += (p*len(region))
        
print(count)