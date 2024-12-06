file = open('input.txt', 'r')
lines = file.read().strip().split()


u, d, ri, le = True, False, False, False

for r in range(len(lines)):
    for c in range(len(lines[0])):
        if lines[r][c] == '^':
            row = r
            col = c
            break
            


def isObstacle(sq):
    if sq != '.' and sq != '^':
        return True
    return False

count = 0


visited = []
visited.append((row, col))

while row >= 0 and row < len(lines) and col >= 0 and col < len(lines[0]):
    print(row,)
    if ri:
        col += 1
        if col < len(lines[0]) and isObstacle(lines[row][col]):
            col -= 1
            d = True
            ri = False
        else:
            if ((row, col) not in visited):
                visited.append((row, col))
                count += 1
    elif le:
        col -= 1
        if col >= 0 and isObstacle(lines[row][col]):
            col += 1
            u = True
            le = False
        elif ((row, col) not in visited):
            visited.append((row, col))
            count += 1
    elif u:
        row -= 1
        if row >= 0 and isObstacle(lines[row][col]):
            row += 1
            ri = True
            u = False
        elif ((row, col) not in visited):
            visited.append((row, col))
            count += 1
    elif d:
        row += 1
        if row < len(lines) and isObstacle(lines[row][col]):
            row -= 1
            le = True
            d = False
        elif ((row, col) not in visited):
            visited.append((row, col))
            count += 1


print(count)
