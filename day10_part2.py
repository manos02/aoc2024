file = open('input.txt', 'r')
lines = file.readlines()


grid = [line.strip() for line in lines]
grid = [list( map(int,i) ) for i in grid]


def follow(grid, pos, goal):

    if pos == goal:
        return 1
    
    r, c = pos

    c_height = grid[r][c]

    f, down, up, left, right = 0, 0, 0, 0, 0

    if r+1 < len(grid) and grid[r+1][c] == c_height + 1: # down
        f = 1
        down = follow(grid, (r+1, c), goal)
    
    if r-1 >= 0 and grid[r-1][c] == c_height + 1: # up
        f = 1
        up = follow(grid, (r-1, c), goal)
    
    if c+1 < len(grid[0]) and grid[r][c+1] == c_height + 1: # right
        f = 1
        right = follow(grid, (r, c+1), goal)
    
    if c-1 >= 0 and grid[r][c-1] == c_height + 1: # left
        f = 1
        left = follow(grid, (r, c-1), goal)

    if not f:
        return 0
    
    return down + up + right + left

     


starting, ending = [], []

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 0:
            starting.append((r,c))
        elif grid[r][c] == 9:
            ending.append((r, c))

count = 0

for s in starting:
    for e in ending:
        
        
        count += follow(grid, s, e)
        

print(count)