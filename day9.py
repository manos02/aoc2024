file = open('input.txt', 'r')
lines = file.readline().strip()

id = 0
res = []
s = 0 # final result
m = 0

for l in range(0, len(lines)):

    if  l % 2 == 0:
        res.extend([id] * int(lines[l]))
        id += 1

    else:
        res.extend([-1] * int(lines[l]))
    

while True:
    if not res:
        break

    if res[0] != -1:
        s += (res[0] * m)
        res.pop(0)
        
    else:
        while True:
            if res[-1] != -1:
                break
            else:
                res.pop(-1)
        s += (res[-1] * m)
        res.pop(-1)
        res.pop(0)

    m += 1

print(s)
