from heapq import heapify, heappop, heappush
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up


f = open("input.txt", 'r')
f = f.read().strip()


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up


def djikstra(source):
    
    pq = [(0, source[0], source[1])]
    heapify(pq)

    dist = {}
    
    for i in range(R):
        for j in range(C):
            if (i,j) not in obs:
                dist[(i,j)] = float('inf')

    
    dist[source] = 0

    while pq:
        current_distance, cx, cy = heappop(
               pq
        )

        if (cx, cy) == (R-1,C-1): # found bottom right
            break

        neigbours = []

        for direction in directions:
            neigbours.append((cx + direction[0], cy+direction[1]))

        for nei in neigbours:
            if 0 > nei[0] or nei[0] >= R or 0 > nei[1] or nei[1] >= C or (nei[0], nei[1]) in obs:
                continue
            
            temp_dist = 1 + current_distance
            
            if temp_dist < dist[(nei[0], nei[1])]:
                dist[(nei[0], nei[1])] = temp_dist
                 
                heappush(pq, (temp_dist, nei[0], nei[1]))
            

    return dist      



orig_obs = []

f = f.split('\n')

for l in f:
    x, y = l.split(",")
    orig_obs.append((int(y), int(x)))


R = 71
C = 71

i = 0
while True:

    if i == len(orig_obs):
        break

    obs = orig_obs[:2900+i]

    visited = djikstra((0,0))
    res = visited[R-1, C-1]

    if res == float('inf'):
        y,x = obs[-1]
        print(x,y)
        break

    i+=1
    

