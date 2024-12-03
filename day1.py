file = open('input.txt', 'r')
lines = file.readlines()

list1, list2 = [], []

for i in lines:
    list1.append(int(i.split()[0]))
    list2.append(int(i.split()[1]))
    
list1.sort()
list2.sort()

total = 0
for i in range(len(list1)):
    total += abs(list1[i] - list2[i])
    
print(total)