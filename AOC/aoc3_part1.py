import re

def calculate_mul_sum(file_path):
    # Read the content of the input file
    with open(file_path, 'r') as file:
        data = file.read()

    # Regular expression to identify valid mul(X,Y) instructions
    mul_pattern = r"mul\((\d+),(\d+)\)"
    
    # Find all matches in the input file
    matches = re.findall(mul_pattern, data)
    
    # Calculate the sum of the results of valid mul operations
    total_sum = sum(int(x) * int(y) for x, y in matches)
    
    return total_sum

# Example usage:
file_path = 'aoc3_part1.txt'  # Replace with your actual file path
result = calculate_mul_sum(file_path)
print(f"The sum of valid mul operations is: {result}")