import re

def calculate_conditional_mul_sum(file_path):
    # Read the content of the input file
    with open(file_path, 'r') as file:
        data = file.read()

    # Regular expressions to match instructions
    mul_pattern = r"mul\((\d+),(\d+)\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    # Track whether mul instructions are enabled (default: enabled)
    mul_enabled = True
    total_sum = 0

    # Process the input data
    position = 0
    while position < len(data):
        # Match `do()` or `don't()`
        if match := re.match(do_pattern, data[position:]):
            mul_enabled = True
            position += match.end()
        elif match := re.match(dont_pattern, data[position:]):
            mul_enabled = False
            position += match.end()
        # Match valid `mul(X,Y)`
        elif mul_enabled and (match := re.match(mul_pattern, data[position:])):
            x, y = map(int, match.groups())
            total_sum += x * y
            position += match.end()
        else:
            # Move to the next character if no valid instruction is found
            position += 1

    return total_sum


# Example usage:
file_path = 'aoc3_part2.txt'  # Replace with your actual file path
result = calculate_conditional_mul_sum(file_path)
print(f"The sum of enabled mul operations is: {result}")