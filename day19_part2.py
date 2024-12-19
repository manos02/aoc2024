
f = open("input.txt", "r")
f = f.read().strip()

towels = []
patterns = []
towels = f.split("\n\n")[0].split(",")
towels = [x.strip() for x in towels]

patterns = f.split("\n\n")[1].split()


res = max(towels, key = len)
MAX_LEN_TOWEL = len(res)
DP = {}

def solve(pattern):

    if len(pattern) == 0:
        return 1

    c = 0

    for i in range(1, MAX_LEN_TOWEL+1):
        if i <= len(pattern) and pattern[:i] in towels:
                
            if pattern[i:] in DP:
                c += DP[pattern[i:]]
                continue
            
            res = solve(pattern[i:]) 
            c += res
            DP[pattern[i:]] = res
    
    return c


count = 0
for i, p in enumerate(patterns):

    count += solve(p)

print(count)