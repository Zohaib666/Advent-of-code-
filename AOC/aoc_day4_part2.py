def count_x_mas(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Check if a given 3-character sequence matches "MAS" or "SAM"
    def matches(sequence):
        return sequence == "MAS" or sequence == "SAM"

    # Check for an X-MAS centered at (r, c)
    def is_x_mas_center(r, c):
        # Ensure enough space for diagonals
        if r - 1 < 0 or r + 1 >= rows or c - 1 < 0 or c + 1 >= cols:
            return False
        # Extract diagonals
        diagonal1 = grid[r - 1][c - 1] + grid[r][c] + grid[r + 1][c + 1]  # Top-left to bottom-right
        diagonal2 = grid[r - 1][c + 1] + grid[r][c] + grid[r + 1][c - 1]  # Top-right to bottom-left
        # Check if both diagonals are valid
        return matches(diagonal1) and matches(diagonal2)

    # Iterate over the grid and count X-MAS patterns
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if is_x_mas_center(r, c):
                count += 1

    return count


# Read the input file
with open("day4_2.txt", "r") as file:
    grid = [line.strip() for line in file.readlines()]

# Calculate the result
result = count_x_mas(grid)
print("Number of X-MAS patterns:", result)

