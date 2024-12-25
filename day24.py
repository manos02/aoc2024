
f = open("input.txt", "r")
f = f.read().strip()

a,b = f.split("\n\n")


wire_dict = {}

for l in a.split("\n"):
    gate, value = l.split(":")
    wire_dict[gate] = int(value)


flag = True
while flag:
    flag = False
    for l in b.split("\n"):
        g1, operator, g2 = l.split("->")[0].split(' ')[0:3]
        g3 = l.split("->")[1].strip()
        
        if g1 not in wire_dict or g2 not in wire_dict:
            flag = True
            continue
        val1 = wire_dict[g1]
        val2 = wire_dict[g2]
        if operator == 'XOR':
            res = val1 ^ val2
        elif operator == 'AND':
            res = val1 & val2
        else:
            res = val1 | val2
        wire_dict[g3] = res



sorted_dict = {key: value for key, value in sorted(wire_dict.items())}
res = ""

for k,v in sorted_dict.items():
    if k[0] == "z":
        res += str(v)

print(int(res[::-1], 2))