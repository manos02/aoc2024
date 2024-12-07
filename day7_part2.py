
file = open('input.txt', 'r')
lines = file.readlines()

def con(a,b):
    return int(str(a) + str(b))


def addmul(t, x, n, c):
    if c == len(x):
        if n == t:
            return True
        else:
            return False
    
    return addmul(t, x, n*x[c], c+1) or addmul(t, x, n+x[c], c+1) or addmul(t, x, con(n, x[c]), c+1)

counter = 0
for l in lines:
    t, x = l.strip().split(":")
    t = int(t)
    x = x.strip().split()
    x = list(map(lambda x: int(x), x))
    
    if (addmul(t, x, x[0], 1)):
        counter += t
    

print(counter)

