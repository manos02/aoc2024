from heapq import heapify, heappop, heappush


f = open("input.txt", "r")
f = f.read().strip()

g = [list(l) for l in f.split("\n")]

R = len(g)
C = len(g[0])


for r in range(R):
    for c in range(C):
        if g[r][c] == "S":
            sr, sc = r,c
        elif g[r][c] == "E":
            er, ec = r,c



directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up

def create_sequence(prev):
    s = []
    u = er,ec
    if prev[u] != None or u == (er,ec):
        while u != None:
            s.insert(0, u)
            u = prev[u]

    return s


def djikstra(source):
    
    pq = [(0, source[0], source[1])]
    heapify(pq)

    dist = {}
    prev = {}
    
    for i in range(R):
        for j in range(C):
            if (i,j) not in g:
                dist[(i,j)] = float('inf')     
                prev[(i,j)] = None

    dist[source] = 0

    while pq:
        current_distance, cx, cy = heappop(
               pq
        )

        if (cx, cy) == (er,ec): 
            break

        neigbours = []

        for direction in directions:
            neigbours.append((cx+direction[0], cy+direction[1]))

        for nei in neigbours:
            if 0 > nei[0] or nei[0] >= R or 0 > nei[1] or nei[1] >= C or g[nei[0]][nei[1]] == '#':
                continue
            
            temp_dist = 1 + current_distance
            
            if temp_dist < dist[(nei[0], nei[1])]:
                dist[(nei[0], nei[1])] = temp_dist
                prev[(nei[0], nei[1])] = (cx,cy)
                 
                heappush(pq, (temp_dist, nei[0], nei[1]))
            

    return dist, prev

visited, prev = djikstra((sr,sc))



init_best = visited[(er,ec)]

s = create_sequence(prev)

count = 0

SEEN = {}

for pos in s:
    for dir in directions:
        nr = pos[0] + dir[0]
        nc = pos[1] + dir[1]

        if (nr,nc) in SEEN:
            continue
        SEEN[(nr,nc)] = 1
        if 0<=nr<R and 0<=nc<C and g[nr][nc] == '#':

            g[nr][nc] = '.'
            visited = djikstra((sr,sc))[0]
            dist = visited[(er,ec)]
        
            if init_best - dist >= 100:
                count+=1
            g[nr][nc] = '#'

    
print(count)

# print('\n'.join(''.join(str(x) for x in row) for row in g)) # print grid

