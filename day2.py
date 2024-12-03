
def isSafe(report):
    sor = sorted(report)
    rsor = sor[::-1]
    if report != sor and report != rsor:
        return False
    
    for i in range(1, len(report)):
        if abs(report[i] - report[i-1]) <= 0 or  abs(report[i] - report[i-1]) > 3:
            return False
        
    return True

file = open('input.txt', 'r')
lines = file.readlines()
d = []

for l in lines:
    d.append([int(item) for item in l.split()])

    
count = 0
for report in d:
    if isSafe(report):
        count += 1

print(count)