#!/usr/bin/env python3
import re 
from math import pow
from functools import reduce
from dataclasses import dataclass

register=dict()

@dataclass
class Program:
    program: list
    def literal(operand):
        return operand
    


opcode = {0: 'adv', 1: 'bxl', 2: 'bst', 3: 'jnz', 4: 'bxc', 5: 'out', 6: 'bdv', 7: 'cdv'}
#def print_program(program):
#    I = 0 # instruction pointer
#    while I < len(program): 
#        print(f"{opcode[program[I]]} { program[I+1] }")
#        I = I + 2

def print_program(program):
    print(f"Program {program}")
    for i, o in zip(program[0::2],program[1::2]):
        print(f"\t{opcode[i]} {o}")
    print()


def literal(operand):
    return operand

def combo(operand, RA, RB, RC):
    if operand >= 0 and operand < 4: 
        return operand
    elif operand == 4: 
        return RA
    elif operand == 5: 
        return RB
    elif operand == 6:
        return RC
    else:
        raise RuntimeError

def static_precompute(program, RA):
    print(f"precompute R = {RA}, 0, 0")
    RB = RA % 8
    print(f"    BST 4      {RA}, {RB}, 0")
    RB = RB ^ 5
    print(f"    BXL 5      {RA}, {RB}, 0")
    RC = RA // int(pow(2, int(RB)))
    print(f"    CDV 5      {RA}, {RB}, {RC}")
    RB = RB ^ 6
    print(f"    BXL 6      {RA}, {RB}, {RC}")
    RA = RA // 8 
    print(f"    ADV 3      {RA}, {RB}, {RC}")
    RB = RB ^ RC
    print(f"    BXC 2      {RA}, {RB}, {RC}")
    print(f"    OUT 5      {RB % 8 }")
    return int(RB % 8)

def compute(program, RA = 0, RB = 0, RC = 0, single=False):
    I = 0
    output = list()

    while I < len(program):
        instruction = opcode[program[I]]
        operand = program[I+1]
        if instruction == 'adv':
            RA = int(RA) // int(pow(2, combo(operand, RA, RB, RC)))
        elif instruction == 'bxl':
            RB = RB ^ literal(operand)
        elif instruction == 'bst':
            RB = int(combo(operand, RA, RB, RC)) % 8
        elif instruction == 'jnz':
            if RA != 0:
                I = literal(operand)
                continue
        elif instruction == 'bxc':
            RB = RB ^ RC
        elif instruction == 'out':
            output.append(int(combo(operand, RA, RB, RC) % 8))
            if single:
                return int(output[-1])
        elif instruction == 'bdv':
            RB = int(RA) // int(pow(2, combo(operand, RA, RB, RC)))
        elif instruction == 'cdv': 
            RC = int(RA) // int(pow(2, combo(operand, RA, RB, RC)))
        else:
            raise RuntimeError('Unknown Operation: {instruction}')
        I = I + 2
    return output

def validate(l1, l2):
    return reduce(lambda x, y: x and y, map(lambda p, q: p == q, l1, l2), True)


def brute_force_approach(program):
    l = len(program)
    l1 = int(pow(8,l-1))
    l2 = int(pow(8,l))
    print(f"Bruteforce between {l1} and {l2}")
    for A in range(l1,l2):
        test = compute(program,A)
        if test == program:
            print(f"GOTCHA: A = {A}")
            return A


def recursive_approach(program, candidates, idx):
    print(f"recursive: {idx:2} : {candidates}")

    if idx == len(program):
        print(f"min candidate: {min(candidates)}")
        return min(candidates)
    
    new_candidates = set()
    for A in candidates: 
        tbytes = [ (A * 8) + x for x in range(0, 8)]
        for i in tbytes:
            if compute(program, i, 0, 0) == program[-1*(idx+1):]:
                new_candidates.add(i)
    
    if len(new_candidates) > 0:
       print(f"new cdt: {new_candidates}")
       return recursive_approach(program, new_candidates, idx + 1)
        
def combination_lock_approach(program):
    l = int(len(program))
    A = 0
    for idx in range(0, l):
        ridx = l - 1 - idx
        tbytes = [ (A * 8) + x for x in range(0, 8)]
        print(f"block {idx}: tbytes ({len(tbytes)}) {tbytes}")
        print(f"target: {program[-1*(idx+1):]}")

        solutions = list()

        for i in tbytes:
            test = compute(program, i, 0, 0)
            print(f"bit {i} {i:b}: {test}")
            if test == program[-1*(idx+1):]:
                solutions.append(i)
        print(f"solutions: {solutions}")
        
        if len(solutions) == 0:
            print(f"NO SOLUTIONS on STEP {idx}")
            return A

        A = min(solutions)

    return A

if __name__ == "__main__":
    with open('input.txt') as file:
        for line in file:
            if m := re.match(r"Register A: (\d+)", line):
                register['RA'] = int(m.group(1))
            if m := re.match(r"Register B: (\d+)", line):
                register['RB'] = int(m.group(1))
            if m := re.match(r"Register C: (\d+)", line):
                register['RC'] = int(m.group(1))
            if line.startswith('Program:'):
                program = list(map(int,re.findall(r'(\d)',line.rstrip().split(':')[1])))

    print_program(program)
    print(f"output: {','.join(list(map(str,compute(program,**register))))}")

    print("==== FIND SEED VALUE ====")
    # find which value of A produces a certain singular output.
    # A needs to be larger than pow(8, len(program)-1): 35184372088832
    A = 0
    L = len(program)
    print(f"Lenght of Program: {L}")
    print(f"          in Bits: {L*3}")
   
    A = recursive_approach(program,list(range(0,8)), 0)
#    A = combination_lock_approach(program) 
#    A = brute_force_approach(program)

    print(f"\nFinal A: {A}\n")

    print(f"\n==== TEST THE RESULT {A} ====\n")
    test = compute(program, A, 0, 0)
    print(f"A = {A}\n\t: {program}\n\t: {test}")
    if validate(test, program):
        print("TRUEEEE")
    else:
        print("FALSEEE")


    # SMALLER THAN 4986088122145496 !!
