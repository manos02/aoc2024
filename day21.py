from itertools import permutations, product

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


def generate_ways(code, k):

    current_location = k['A']

    valid_paths = []

    for c in code:

        next_location = k[c]
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

        
def solve(code):
    

    w = generate_ways(code, NUMERIC_KEYBOARD)
    w2 = []
    w3 = []
    for way in w:
        w2 += generate_ways(way, DIRECTIONAL_KEYBOARD)
        
    for way in w2:
        w3 += generate_ways(way, DIRECTIONAL_KEYBOARD)


    return min([len(x) for x in w3])


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