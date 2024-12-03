import re 

file = open('input.txt', 'r')
str = file.read()

x = re.findall('mul\(\d+,\d+\)|do\(\)|don\'t\(\)', str)

discard = False

new_x = []
for i in range(len(x)):
    if x[i] == "don't()":
        discard = True
    elif x[i] == "do()":
        discard = False
    else:
        if not discard:
            new_x.append(x[i])
y = []

for i in range(len(new_x)):
    y.append(re.findall(r'\d+', new_x[i]))

res = sum(list(map(lambda n: int(n[0]) * int(n[1]), y)))
print(res)