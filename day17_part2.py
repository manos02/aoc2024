
f = open("input2.txt", "r")
f = f.read().strip()
f = f.split("\n")

def combo(operand, regA, regB, regC):
    if operand >= 0 and operand <= 3:
        return operand
    elif operand == 4:
        return regA
    elif operand == 5:
        return regB
    elif operand == 6:
        return regC
    

def run_program(program, init_a):
    finish = []
    i = 0

    regA = init_a
    regB = 0
    regC = 0

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
            
            finish.append(res)
            
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

    return finish

def reverse_eng(loop, target, a_s=0): # target is our program

    if target == []: # base case
        return a_s
    
    for cand in (a_s * 8 + next_3_bits for next_3_bits in range(8)):
        last = run_program(loop, cand).pop()
        if last == int(target[-1]):
            # print(cand)
            r = reverse_eng(loop, target[:-1], cand)
            if r != None:
                return r
            else:
                continue
    return None


program = []

regA = int(f[0].split(":")[1])
regB = int(f[1].split(":")[1])
regC = int(f[2].split(":")[1])
program = (f[4].split(":")[1]).strip().split(",")


loop = program[:-2] # remove 3,0 pair 
initial_a = reverse_eng(loop, program)
print(initial_a)

# print(run_program(program, initial_a))
# print(run_program(program, 392))



