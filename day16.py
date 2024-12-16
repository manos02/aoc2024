from heapq import heapify, heappop, heappush


f = open("input2.txt", 'r')
f = f.read().strip()

g = [list(l) for l in f.split("\n")]

R = len(g)
C = len(g[0])


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up



def djikstra(source, initial_direction):
    
    pq = [(0, source[0], source[1], initial_direction)]
    heapify(pq)


    while pq:
        current_distance, cx, cy, direction = heappop(
               pq
        )

        neigbours = []

        neigbours.append((cx + directions[direction][0],  cy + directions[direction][1], direction))
        neigbours.append((cx + directions[(direction + 1) % 4][0],  cy + directions[(direction + 1) % 4][1], (direction + 1) % 4))
        neigbours.append((cx + directions[(direction + 3) % 4][0],  cy + directions[(direction + 3) % 4][1], (direction + 3) % 4))

        for nei in neigbours:
            if 0 > nei[0] or nei[0] >= R or 0 > nei[1] or nei[1] >= C or g[nei[0]][nei[1]] == "#":
                continue
            temp_dist = 1 + current_distance if nei[2] == direction else 1001 + current_distance
            if temp_dist < dist[(nei[0], nei[1])]:
                dist[(nei[0], nei[1])] = temp_dist
                
                
                paths[(nei[0], nei[1])] = [[]]

                total_list = []

                for path in paths[(cx, cy)]:

                    li = path.copy()
                    li.append((nei[0], nei[1]))
                    
                    total_list.append(li)

                paths[(nei[0], nei[1])] = total_list

                heappush(pq, (temp_dist, nei[0], nei[1], nei[2]))

       
                
dist = {}
paths = {}

for i in range(R):
    for j in range(C):

        if g[i][j] != "#":
            dist[(i,j)] = float('inf')
            paths[(i, j)] = []

        if g[i][j] == 'S':
            sr, sc = i, j
        if g[i][j] == 'E':
            er, ec = i, j

dist[(sr, sc)] = 0
paths[(sr, sc)] = []

direction = 0
paths[(sr, sc)] = [[(sr, sc)]]


djikstra((sr, sc), direction)


total = dist[(er, ec)]
print(total)




