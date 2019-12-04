INPUT = [
    1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,13,19,23,2,23,9,27,
    1,6,27,31,2,10,31,35,1,6,35,39,2,9,39,43,1,5,43,47,2,47,13,51,
    2,51,10,55,1,55,5,59,1,59,9,63,1,63,9,67,2,6,67,71,1,5,71,75,
    1,75,6,79,1,6,79,83,1,83,9,87,2,87,10,91,2,91,10,95,1,95,5,99,
    1,99,13,103,2,103,9,107,1,6,107,111,1,111,5,115,1,115,2,119,1,
    5,119,0,99,2,0,14,0
]

MUTATED_INPUT = [
    1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,13,19,23,2,23,9,27,
    1,6,27,31,2,10,31,35,1,6,35,39,2,9,39,43,1,5,43,47,2,47,13,51,
    2,51,10,55,1,55,5,59,1,59,9,63,1,63,9,67,2,6,67,71,1,5,71,75,
    1,75,6,79,1,6,79,83,1,83,9,87,2,87,10,91,2,91,10,95,1,95,5,99,
    1,99,13,103,2,103,9,107,1,6,107,111,1,111,5,115,1,115,2,119,1,
    5,119,0,99,2,0,14,0
]

# Part 1
# Core
def intcode(opcode):
    i = 0
    while i < len(opcode):
        if opcode[i] == 1:
            opcode = intcode_add(opcode=opcode, index=i)
            i += 4
        elif opcode[i] == 2:
            opcode = intcode_multiply(opcode=opcode, index=i)
            i += 4
        elif opcode[i] == 99:
            i = len(opcode)
    return opcode

def intcode_add(opcode, index):
    opcode[opcode[index + 3]] = opcode[opcode[index + 1]] + opcode[opcode[index + 2]]
    return opcode


def intcode_multiply(opcode, index):
    opcode[opcode[index + 3]] = opcode[opcode[index + 1]] * opcode[opcode[index + 2]]
    return opcode

# Tests
def test_intcode():
    assert intcode([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50]


def test_intcode_add():
    assert intcode_add([1,0,0,0,99], index=0) == [2,0,0,0,99]


def test_intcode_multiply():
    assert intcode_multiply([2,3,0,3,99], index=0) == [2,3,0,6,99]

# Part 2
# Core


# Tests


# Exec
print(intcode(MUTATED_INPUT))