
f = open("input2.txt", "r")
f = f.read().strip()
f = f.split("\n")


program = []

regA = int(f[0].split(":")[1])
regB = int(f[1].split(":")[1])
regC = int(f[2].split(":")[1])
program = (f[4].split(":")[1]).strip().split(",")


def combo(operand, regA, regB, regC):
    if operand >= 0 and operand <= 3:
        return operand
    elif operand == 4:
        return regA
    elif operand == 5:
        return regB
    elif operand == 6:
        return regC

i = 0
while i < len(program) - 1:

    opcode = int(program[i])
    operand = int(program[i+1])
    
    if opcode == 0:
        numerator = regA
        denominator = combo(operand, regA, regB, regC)
        res = numerator // (2**denominator)
        regA = res
        
    elif opcode == 1:
        regB = regB ^ operand

    elif opcode == 2:
        
        regB = (combo(operand, regA, regB, regC) % 8)
    elif opcode == 3:
        if regA == 0:
            pass
        else:
            i = operand
            continue
        
        
    elif opcode == 4:
        regB = regB ^ regC
    elif opcode == 5:
        res = (combo(operand, regA, regB, regC) % 8)
        print(res, end = ",")
    elif opcode == 6:
        numerator = regA
        denominator = combo(operand, regA, regB, regC)
        res = numerator // (2**denominator)
        regB = res
    elif opcode == 7:
        numerator = regA
        denominator = combo(operand, regA, regB, regC)
        res = numerator // (2**denominator)
        regC = res

    i+=2
    

