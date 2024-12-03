file = open('input.txt', 'r')
lines = file.readlines()

list1, list2 = [], []

for i in lines:
    list1.append(int(i.split()[0]))
    list2.append(int(i.split()[1]))
    
total = 0
for j in range(len(list1)):
    total += list2.count(list1[j]) * list1[j]

print(total)