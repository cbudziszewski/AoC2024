#!/usr/bin/env python3
import re 
from math import pow

register=dict()

opcode = {0: 'adv', 1: 'bxl', 2: 'bst', 3: 'jnz', 4: 'bxc', 5: 'out', 6: 'bdv', 7: 'cdv'}
def print_program(program):
    I = 0 # instruction pointer
    while I < len(program): 
        print(f"{opcode[program[I]]} { program[I+1] }")
        I = I + 2

def literal(operand):
    return operand

def combo(operand):
    if operand >= 0 and operand < 4: 
        return operand
    elif operand == 4: 
        return register['A']
    elif operand == 5: 
        return register['B']
    elif operand == 6:
        return register['C']
    else:
        raise RuntimeError

def compute(program):
    I = 0
    output = list()
    print(register)

    while I < len(program):
        instruction = opcode[program[I]]
        operand = program[I+1]
        if instruction == 'adv':
            print(f"adv {operand}: A := A // 2^^{combo(operand)} = {int(register['A']) // int(pow(2, combo(operand)))}")
            register['A'] = int(register['A']) // int(pow(2, combo(operand)))
        elif instruction == 'bxl':
            print(f"bxl {operand}: B = B ^ {literal(operand)} = {register['B'] ^ literal(operand)}")
            register['B'] = register['B'] ^ literal(operand)
        elif instruction == 'bst':
            print(f"bst {operand}: B:= {combo(operand)} % 8 = {int(combo(operand)) % 8}")
            register['B'] = int(combo(operand)) % 8
        elif instruction == 'jnz':
            print(f"jnz {register['A']} {literal(operand)}")
            if register['A'] != 0:
                I = literal(operand)
                continue
        elif instruction == 'bxc':
            print(f"bxc {operand}: B = B ^ C : {register['B'] ^ register['C']}")
            register['B'] = register['B'] ^ register['C']
        elif instruction == 'out':
            print(f"out {operand}: {combo(operand)} % 8 = {int(operand) % 8}")
            output.append(int(combo(operand) % 8))
        elif instruction == 'bdv':
            print(f"bdv {operand}: B = A // 2^^{combo(operand)} = {int(register['A']) // int(pow(2, combo(operand)))}")
            register['B'] = int(register['A']) // int(pow(2, combo(operand)))
        elif instruction == 'cdv': 
            print(f"cdv {operand}: C = A // 2^^{combo(operand)} = {int(register['A']) // int(pow(2, combo(operand)))}")
            register['C'] = int(register['A']) // int(pow(2, combo(operand)))
        else:
            raise RuntimeError('Unknown Operation: {instruction}')

        I = I + 2
        print(register)

    print(f"\noutput: {','.join(list(map(str,output)))}")
        
if __name__ == "__main__":
    with open('input.txt') as file:
        for line in file:
            if m := re.match(r"Register A: (\d+)", line):
                register['A'] = int(m.group(1))
            if m := re.match(r"Register B: (\d+)", line):
                register['B'] = int(m.group(1))
            if m := re.match(r"Register C: (\d+)", line):
                register['C'] = int(m.group(1))
            if line.startswith('Program:'):
                program = list(map(int,re.findall(r'(\d)',line.rstrip().split(':')[1])))

    print_program(program)
    print()
    compute(program)
