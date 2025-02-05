import re
from collections import *
import numpy as np

# Directly using the given input values
a = 47719761 # Register A
b = 0         # Register B
c = 0         # Register C
prog = [2,4,1,5,7,5,0,3,4,1,1,6,5,5,3,0]  # Program sequence

# Function to handle the program logic
def run(prog, a, b, c):
    def combo(num):
        if num <= 3:
            return num
        elif num == 4:
            return a
        elif num == 5:
            return b
        elif num == 6:
            return c

    o = []
    ip = 0
    while ip < len(prog):
        instr = prog[ip]
        operand = prog[ip + 1]
        if instr == 0:
            a = a // (2 ** combo(operand))
        elif instr == 1:
            b = b ^ operand
        elif instr == 2:
            b = combo(operand) % 8
        elif instr == 3:
            if a != 0:
                ip = operand - 2
        elif instr == 4:
            b = b ^ c
        elif instr == 5:
            o.append(combo(operand) % 8)
        elif instr == 6:
            b = a // (2 ** combo(operand))
        elif instr == 7:
            c = a // (2 ** combo(operand))
        ip += 2
    return o

# Run the program and print the output
print("Output:", *run(prog, a, b, c), sep=",")

# Recursive function to find a solution
def rec(n, a):
    if n == -1:
        return a
    a <<= 3
    for x in range(8):
        if run(prog, a + x, 0, 0) == prog[n:]:
            s = rec(n - 1, a + x)
            if s != -1:
                return s
    return -1

# Print the result of the recursive function
print("Result:", rec(len(prog) - 1, 0))

     
