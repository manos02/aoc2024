file = open('input.txt', 'r')
lines = file.readline().strip()

id = 0
res = []
s = 0 # final result
m = 0
r = []

for l in range(0, len(lines)):

    if  l % 2 == 0:
        res.append([id, int(lines[l])])
        id += 1
    else:
        res.append([-1,  int(lines[l])])
    
i = 0
f = True
flag = True


flag = False
for i in range(len(res)):
    n, f = res[i]        
    if n == -1:
        j = -1
        while True:
            if res[j][0] != -1 and res[j][1] <= f:
                res[i][1] -= res[j][1]
                t = res[j]
                res[j] = [-1, res[j][1]]
                res.insert(i, t)
                break
            elif abs(j) == len(res) - i:
                break
            else:
                j -= 1

for i in res:
    if i[1] != 0 and i[0] != -1:
        for z in range(i[1]):
            s += (i[0]*m)
            m += 1
    elif i[0] == -1:
        m += i[1] 

print(s)