from collections import deque

f = open("input.txt", "r")
f = f.read().strip()

a,b = f.split("\n\n")

wire_dict = {}

for l in a.split("\n"):
    gate, value = l.split(":")
    wire_dict[gate] = int(value)

# print(wire_dict)
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



print(instructions)


def find(operand, xi, yi):
    for inst in instructions:
        if inst[2] == operand and (inst[0] == xi or inst[0] == yi) and  (inst[1] == xi or inst[1] == yi):
            return inst[3]
        
    return None



for i in range(45):
    i = bin(6)[2:]

    and_res = find("XOR", f"x{i}", f"y{i}")
    and_res = find("AND", f"x{i}", f"y{i}")
    









# def solve(instructions):
#     flag = True
#     while flag:
#         flag = False
#         for g1,g2,operator, g3 in instructions:        
#             if g1 not in wire_dict or g2 not in wire_dict:
#                 flag = True
#                 continue
#             val1 = wire_dict[g1]
#             val2 = wire_dict[g2]
#             if operator == 'XOR':
#                 res = val1 ^ val2
#             elif operator == 'AND':
#                 res = val1 & val2
#             else:
#                 res = val1 | val2
#             wire_dict[g3] = res


# solve(instructions)

# sorted_dict = {key: value for key, value in sorted(wire_dict.items())}
# res = ""

# for k,v in sorted_dict.items():
#     if k[0] == "z":
#         res += str(v)



# wrong_res = bin(int(res[::-1], 2))
# correct_res = bin(int(x, 2) + int(y, 2))



# l = {}
# for i in range(0, len(correct_res)-2):
#     if correct_res[::-1][i] != wrong_res[::-1][i]:
#         l[i] = correct_res[::-1][i]
        



