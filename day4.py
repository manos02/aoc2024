file = open('input.txt', 'r')
lines = file.read().strip().split()

count = 0
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "X":
            if j + 3 < len(lines[0]) and lines[i][j+1:j+4] == "MAS": # horizontal
                count += 1
               
            if j - 3 >= 0 and lines[i][j-1:j-4:-1] == "MAS": # backwards
                count += 1

            if i + 3 < len(lines): # vertical down
                isMas = ''
                for k in range(1, 4):
                    isMas += lines[i+k][j]
                if isMas == "MAS":
                    count += 1
    
            if i - 3 >= 0: # vertical up
                isMas = ''
                for k in range(1, 4):
                    isMas += lines[i-k][j]
                if isMas == "MAS":
                    count += 1

            # diagonal down right
            if j + 3 < len(lines[0]) and i + 3 < len(lines):
                isMas = ''
                for k in range(1, 4):
                    isMas += lines[i+k][j+k]

                if isMas == "MAS":
                    count += 1
            
            if j - 3 >= 0 and i - 3 >= 0:
                isMas = ''
                for k in range(1, 4):
                    isMas += lines[i-k][j-k]

                if isMas == "MAS":
                    count += 1

            if j + 3 < len(lines[0]) and i - 3 >= 0:
                isMas = ''
                for k in range(1, 4):
                    isMas += lines[i-k][j+k]

                if isMas == "MAS":
                    count += 1

            if j - 3 >= 0 and i + 3 < len(lines):
                isMas = ''
                for k in range(1, 4):
                    isMas += lines[i+k][j-k]

                if isMas == "MAS":
                    count += 1

print(count)