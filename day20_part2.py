from heapq import heapify, heappop, heappush


f = open("input2.txt", "r")
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
    steps = 0
    s = []
    u = er,ec
    if prev[u] != None or u == (er,ec):
        while u != None:
            s.insert(0, (u,steps))
            steps+= 1
            u = prev[u]

    return s


def manhattan_distance(s,e):
    return abs(s[0]-e[0]) + abs(s[1]-e[1])


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
initial_path = create_sequence(prev)
len_orig_path = len(initial_path)

count = 0
num_steps = 0
for step in range(len(initial_path)):
    r,c = initial_path[step][0]

    for next_step in range(step+1, len(initial_path)):
        nr, nc = initial_path[next_step][0]
        
        new_dist = manhattan_distance((r,c), (nr,nc))
        distance_to_end = initial_path[next_step][1]
                
        
        if new_dist <= 20 and len_orig_path - (manhattan_distance((r,c), (nr,nc)) + num_steps + distance_to_end) >= 100:
            count += 1

    num_steps += 1


print(count)

