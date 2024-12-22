
f = open("input.txt", "r")
f = f.read().strip().split("\n")
secret_numers = [int(x) for x in f]

total = 0
for s in secret_numers:

    for i in range(2000):
        temp_s = s * 64
        s = s ^ temp_s
        s = s%16777216
        temp_s = s // 32
        s = s ^ temp_s
        s = s%16777216
        temp_s = 2048*s
        s = s^temp_s
        s = s%16777216
    total += s
    
print(total)