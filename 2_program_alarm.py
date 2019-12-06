INPUT = [
    1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,13,19,23,2,23,9,27,
    1,6,27,31,2,10,31,35,1,6,35,39,2,9,39,43,1,5,43,47,2,47,13,51,
    2,51,10,55,1,55,5,59,1,59,9,63,1,63,9,67,2,6,67,71,1,5,71,75,
    1,75,6,79,1,6,79,83,1,83,9,87,2,87,10,91,2,91,10,95,1,95,5,99,
    1,99,13,103,2,103,9,107,1,6,107,111,1,111,5,115,1,115,2,119,1,
    5,119,0,99,2,0,14,0
]


# Part 1
# Core
def process_addition(opcode, index):
    opcode[opcode[index + 3]] = add(value_a=opcode[opcode[index + 1]], value_b=opcode[opcode[index + 2]])
    return opcode, index + 4


def process_multiplication(opcode, index):
    opcode[opcode[index + 3]] = multiply(value_a=opcode[opcode[index + 1]], value_b=opcode[opcode[index + 2]])
    return opcode, index + 4


def process_kill(opcode, index):
    return opcode, len(opcode)


OPERATION_CORRESPONDANCE = {
    1: process_addition,
    2: process_multiplication,
    99: process_kill
}


def intcode(opcode):
    i = 0
    while i < len(opcode):
        opcode, i = OPERATION_CORRESPONDANCE[opcode[i]](
            opcode=opcode,
            index=i
        )
    return opcode


def add(value_a, value_b):
    return value_a + value_b


def multiply(value_a, value_b):
    return value_a * value_b


# Tests
def test_intcode():
    assert intcode([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50]


def test_add():
    assert add(2, 4) == 6
    assert add(19273, 7218) == 26491


def test_multiply():
    assert multiply(4, 3) == 12
    assert multiply(13, 11) == 143


def test_process_addition():
    assert process_addition([1,0,0,0,99], index=0) == ([2,0,0,0,99], 4)


def test_process_multiplication():
    assert process_multiplication([2,3,0,3,99], index=0) == ([2,3,0,6,99], 4)


# Part 2
# Core


# Tests


# Exec
def find_part_1_answer():
    mutated_input = INPUT.copy()
    mutated_input[1] = 12
    mutated_input[2] = 2
    return intcode(mutated_input)[0]

print(find_part_1_answer())  # -> 2894520


def generate_pairs(n):
    for i in range(n):
        for j in range(n):
            yield i, j


def find_specific_operation():
    for noun, verb in generate_pairs(100):
        mutated_input = INPUT.copy()
        mutated_input[1] = noun
        mutated_input[2] = verb
        if intcode(mutated_input)[0] == 19690720:
            return 100 * noun + verb


print(find_specific_operation())