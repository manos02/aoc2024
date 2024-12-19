
f = open("input.txt", "r")
f = f.read().strip()

towels = []
patterns = []
towels = f.split("\n\n")[0].split(",")
towels = [x.strip() for x in towels]

patterns = f.split("\n\n")[1].split()


def solve(pattern, pointer):

    if pointer >= len(pattern):
        return True

    sol = False
    for t in towels:                 
        if t == pattern[pointer:pointer+len(t)]:
            sol = solve(pattern, pointer+len(t)) or sol
            if sol == True:
                break
    
    return sol


count = 0
for p in patterns:

    if (solve(p, 0)):
        count += 1

print(count)