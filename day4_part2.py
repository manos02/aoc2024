file = open('input.txt', 'r')
lines = file.read().strip().split()



count = 0
for i in range(len(lines)-2):
    for j in range(len(lines[0])-2):
        diag1 = ""
        diag1 = lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2]
        diag2 = lines[i][j+2] + lines[i+1][j+1] + lines[i+2][j]
        
        if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
            count += 1


print(count)