from collections import defaultdict

file = open('input.txt', 'r')
stones = file.readlines()
stones = stones[0].split()


CACHE = {}

def solve(stone, level):
    
    if (stone, level) in CACHE:
        return CACHE[(stone, level)]
    
    if level == 75:
        return 1

    if stone == '0':
        res = solve('1', level + 1)
        CACHE[('0', level)] = res
        return res
    
    elif len(stone) % 2 == 0: # even number
            left_half = stone[:len(stone) // 2]
            right_half = stone[len(stone) // 2:]
            
            right_half = str(int(right_half))
            left_half = str(int(left_half))

            left_res = solve(left_half, level + 1)
            right_res = solve(right_half, level + 1)
            
            CACHE[(stone, level)] = left_res + right_res
            return left_res + right_res
    else:
        s = str(int(stone) * 2024)
        res = solve(s, level + 1)
        CACHE[(stone, level)] = res
        return res


counter = 0
for st in range(len(stones)):
    counter += solve(stones[st], 0)
    
    


        
print(counter)