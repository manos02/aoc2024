
f = open("input.txt", "r")
f = f.read().strip()

a,b = f.split("\n\n")

wire_dict = {}

for l in a.split("\n"):
    gate, value = l.split(":")
    wire_dict[gate] = int(value)


x = ''
y = ''
for k,v in wire_dict.items():
    if k[0] == 'x':
        x += str(v)
    else:
        y += str(v)

x = x[::-1]
y = x[::-1]

correct_res = bin(int(x, 2) + int(y, 2)) # 46  bits in total

instructions = []
for l in b.split("\n"):
    g1, operator, g2 = l.split("->")[0].split(' ')[0:3]
    g3 = l.split("->")[1].strip()
    instructions.append((g1,g2,operator,g3))


def find(operand, xi, yi):
    print(operand, xi, yi)
    for inst in instructions:
        if inst[2] == operand and (inst[0] == xi or inst[0] == yi) and (inst[1] == xi or inst[1] == yi):
            return inst[3]
        
    return None


c0 = None
swapped = []

for i in range(45):
    i = str(i).zfill(2)
    xor_res, and_res, r1, z1, c1 = None, None, None, None, None

    xor_res = find("XOR", f"x{i}", f"y{i}")
    and_res = find("AND", f"x{i}", f"y{i}")

    print(i, xor_res, and_res, c0)
    if c0:
        r1 = find("AND", c0, xor_res)
        if not r1:
            xor_res, and_res = and_res, xor_res
            swapped.extend([xor_res, and_res])
            r1 = find("AND", c0, xor_res)

        z1 = find("XOR", c0, xor_res)


        if xor_res and xor_res.startswith("z"):
            xor_res, z1 = z1, xor_res
            swapped.extend([xor_res, z1])

        if and_res and and_res.startswith("z"):
            and_res, z1 = z1, and_res
            swapped.extend([and_res, z1])

        if r1 and r1.startswith("z"):
            r1, z1 = z1, r1
            swapped.extend([r1, z1])

        c1 = find("OR", r1, and_res)

    if c1 and c1.startswith("z") and c1 != "z45":
        c1, z1 = z1, c1
        swapped.extend([c1, z1])


    c0 = c1 if c0 else and_res

print(",".join(sorted(swapped)))

