from collections import defaultdict

file = open('input.txt', 'r')
lines = file.readlines()

y = defaultdict(list)
p = []


for l in lines:
    if l != '\n':
        x = l.strip().split("|")
        y[x[0]].append(x[1])
    else:
        break

count = 0
for l in reversed(lines):
    if l != '\n':
        x = l.strip().split("|")
        z = x[0].split(",")
        
        v = True
        for i in range(1, len(z)):
            for j in range(i-1, -1, -1):    
                if z[j] in y[z[i]]:
                    v = False
                    break

        if v:
            count += int(z[len(z)//2])
                    
    else:
        break
  

print(count)