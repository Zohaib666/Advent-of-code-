def count_xmas_occurrences(grid, word="XMAS"):
    # Define the possible directions: (dx, dy)
    directions = [
        (1, 0),   # Horizontal, right
        (0, 1),   # Vertical, down
        (1, 1),   # Diagonal, down-right
        (1, -1),  # Diagonal, down-left
        (-1, 0),  # Horizontal, left
        (0, -1),  # Vertical, up
        (-1, -1), # Diagonal, up-left
        (-1, 1)   # Diagonal, up-right
    ]
    
    rows, cols = len(grid), len(grid[0])
    word_length = len(word)
    count = 0

    # Helper function to check if the word exists in a given direction
    def is_word_at(x, y, dx, dy):
        for i in range(word_length):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != word[i]:
                return False
        return True

    # Iterate through each cell in the grid
    for x in range(rows):
        for y in range(cols):
            # Check each direction from this starting point
            for dx, dy in directions:
                if is_word_at(x, y, dx, dy):
                    count += 1

    return count

# Read the input grid from a file
with open("day4_1.txt", "r") as file:
    grid = [line.strip() for line in file]

# Count occurrences of "XMAS"
result = count_xmas_occurrences(grid)

# Output the result
print("Total occurrences of XMAS:", result)
