from collections import defaultdict

f = open("input2.txt", "r")
f = f.read().strip().split("\n")
secret_numers = [int(x) for x in f]

DICT = defaultdict(int)

total = 0
for s in secret_numers:

    seen = {}

    price = int(str(s)[-1])
    sequence_list = []

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

        n_price = int(str(s)[-1])
        diff = n_price - price

        if len(sequence_list) == 4:
            sequence_list.pop(0)    

        sequence_list.append(diff)

        if tuple(sequence_list) not in seen:

            seen[tuple(sequence_list)] = True
            DICT[tuple(sequence_list)] += n_price
        
        price = n_price
    total += s

max_tup = max(DICT, key=DICT.get)
print(DICT[max_tup])
