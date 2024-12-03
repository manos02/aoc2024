import re 

file = open('input.txt', 'r')
str = file.read()


x = re.findall('mul\(\d+,\d+\)', str)

y = []

for i in range(len(x)):
    y.append(re.findall(r'\d+', x[i]))

res = sum(list(map(lambda n: int(n[0]) * int(n[1]), y)))

print(res)