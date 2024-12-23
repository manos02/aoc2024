from collections import defaultdict

f = open("input.txt", 'r')
f = f.read().strip()
f = f.split("\n")

DICT = defaultdict(list)

for link in f:
    a,b = link.split("-")

    DICT[a].append(b)
    DICT[b].append(a)
        
res = []

for k,v in DICT.items():
    for value in v:
        for elem in DICT[value]:
            if elem in v and elem != k:
                temp = []
                temp.append(k)
                temp.append(value)
                temp.append(elem)
                res.append(temp)

for i in range(len(res)):
    res[i] = sorted(res[i])

final = []
t_list = []

for i in res:
    if i not in final:
        final.append(i)


for i in final:
    if i[0][0] == "t" or i[1][0] == "t" or i[2][0] == "t":
        t_list.append(i)


print(len(t_list))

