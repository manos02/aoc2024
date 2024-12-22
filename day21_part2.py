from itertools import permutations, product
from functools import lru_cache

f = open("input.txt", 'r')
f = f.read().strip()
codes = f.split("\n")

NUMERIC_KEYBOARD = {'7':(0,0), '8':(0,1), '9':(0,2), '4':(1,0), '5':(1,1), '6':(1,2), '1':(2,0), '2':(2,1), '3':(2,2), '0':(3,1), 'A':(3,2)}
DIRECTIONAL_KEYBOARD = {"^":(0,1), "v":(1,1), ">":(1,2), "<":(1,0),"A":(0,2)} # up, down, right, left

movedir = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}

directions = {
    "A": (2, 0),
    "^": (-1, 0),
    "<": (0, -1),
    "v": (1, 0),
    ">": (0, 1),
}

@lru_cache(None)
def generate_ways(a, b, k):

    k = DIRECTIONAL_KEYBOARD if k else NUMERIC_KEYBOARD

    current_location = k[a]
    next_location = k[b]


    valid_paths = []

        
    move_row = next_location[0] - current_location[0] 
    move_col = next_location[1] - current_location[1]


    moves = "" # generate one possible path
    if move_row > 0:
        moves += "v" * move_row
    else:
        moves += "^" * -move_row

    if move_col > 0:
        moves += ">" * move_col
    else:
        moves += "<" * -move_col
    
    # generate all paths
    possible_paths = list(set(["".join(x) + "A" for x in permutations(moves)]))

    # check path
    combs = []

    for path in possible_paths:
        cr, cc = current_location
        valid = True
        
        nr,nc = cr, cc
        for step in path[:-1]:
            
            nr = nr + directions[step][0]
            nc = nc + directions[step][1]

            if (nr,nc) not in k.values():
                valid = False
                break

        if valid:        
            combs.append(path)
            
    
    valid_paths.append(combs)
    current_location = next_location
    
    return ["".join(x) for x in product(*valid_paths)] # dot product

@lru_cache(None)
def min_cost(s, k, d=0):

    a = s[0]
    b = s[1]

    if d==0:
        return min([len(x) for x in generate_ways(a, b, True)])
    
    w = generate_ways(a, b, k)
    best_cost = float('inf')
    
    for seq in w:
        seq = "A" + seq
        cost = 0
        path = [(seq[i],seq[i+1]) for i in range(len(seq)-1)]
        for e in path:
            cost += min_cost((e[0], e[1]), True, d-1)

        best_cost = min(best_cost, cost)

    return best_cost


        
def solve(code):

    code = 'A' + code
    cost = 0
    seq = [(code[i],code[i+1]) for i in range(len(code)-1)]

    for s in seq:
        cost += min_cost(s, False, 25)
    
    return cost





total = 0
for c in codes:
    res = solve(c)
    numeric_part = 0
    try:
        numeric_part = int(c[0:3])
    except:
        numeric_part = int(c[1:3])
    total += res*numeric_part

print(total)