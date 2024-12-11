file = open('input.txt', 'r')
stones = file.readlines()


stones = stones[0].split()


for i in range(75):
    f = False
    c = 0
    stone = 0
    while stone < len(stones):

        if stones[stone] == '0':
            stones[stone] = '1'
        elif len(stones[stone]) % 2 == 0: # even number of digits
            num = stones[stone] 
            left_half = num[:len(num) // 2]
            right_half = num[len(num) // 2:]
            
            right_half = str(int(right_half))
            left_half = str(int(left_half))

            stones[stone] = right_half
            stones.insert(stone, left_half)
            
            stone += 1
        else:
            stones[stone] = str(int(stones[stone]) * 2024)
        stone += 1

print(len(stones))
