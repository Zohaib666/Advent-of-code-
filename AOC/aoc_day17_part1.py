def execute_program(registers, program):
    def get_combo_value(operand):
        # Get the appropriate value based on the operand
        if operand <= 3:
            return operand
        elif operand == 4:
            return registers.get('A', 0)
        elif operand == 5:
            return registers.get('B', 0)
        elif operand == 6:
            return registers.get('C', 0)
        else:
            raise ValueError(f"Invalid combo operand: {operand}")

    output = []
    instruction_pointer = 0

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1] if instruction_pointer + 1 < len(program) else 0

        print(f"IP: {instruction_pointer}, Opcode: {opcode}, Operand: {operand}")
        print(f"Before Execution: A={registers['A']}, B={registers['B']}, C={registers['C']}")

        if opcode == 0:  # adv
            denominator = 2 ** get_combo_value(operand)
            registers['A'] //= denominator

        elif opcode == 1:  # bxl
            registers['B'] ^= operand

        elif opcode == 2:  # bst
            registers['B'] = get_combo_value(operand) % 8

        elif opcode == 3:  # jnz
            if registers['A'] != 0:
                instruction_pointer = operand
                print(f"Jumping to {instruction_pointer}")
                continue

        elif opcode == 4:  # bxc
            registers['B'] ^= registers['C']

        elif opcode == 5:  # out
            output.append(get_combo_value(operand) % 8)

        elif opcode == 6:  # bdv
            denominator = 2 ** get_combo_value(operand)
            registers['B'] = registers['A'] // denominator

        elif opcode == 7:  # cdv
            denominator = 2 ** get_combo_value(operand)
            registers['C'] = registers['A'] // denominator

        else:
            raise ValueError(f"Invalid opcode: {opcode}")

        instruction_pointer += 2
        print(f"After Execution: A={registers['A']}, B={registers['B']}, C={registers['C']}")
        print("-" * 30)

    print("Final Registers:", registers)
    return ",".join(map(str, output))

# Read input data
def main():
    # Initializing input values
    registers = {
        "A": 62769524,
        "B": 0,
        "C": 0,
    }

    program = [2, 4, 1, 7, 7, 5, 0, 3, 4, 0, 1, 7, 5, 5, 3, 0]

    # Execute program
    result = execute_program(registers, program)
    print("Output:", result)

if __name__ == "__main__":
    main()
