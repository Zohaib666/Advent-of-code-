import heapq

def parse_input(filename):
    """Parses the input file and returns a list of byte positions."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [tuple(map(int, line.strip().split(','))) for line in lines]

def simulate_corruption(grid_size, byte_positions, max_bytes):
    """Simulates the falling bytes, marking corrupted positions on the grid."""
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]
    for i, (x, y) in enumerate(byte_positions):
        if i >= max_bytes:
            break
        grid[y][x] = "#"
    return grid

def is_valid(x, y, grid):
    """Checks if a position is valid and not corrupted."""
    return 0 <= x < len(grid) and 0 <= y < len(grid) and grid[y][x] == "."

def is_path_possible(grid):
    """Checks if there is a path from the top-left corner to the bottom-right corner."""
    grid_size = len(grid)
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)

    if grid[0][0] == "#" or grid[end[1]][end[0]] == "#":
        return False

    # BFS to check for path
    queue = [start]
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.pop(0)
        if (x, y) == end:
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, grid) and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))

    return False

def find_blocking_byte(grid_size, byte_positions):
    """Finds the first byte that blocks the path to the exit."""
    grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

    for i, (x, y) in enumerate(byte_positions):
        grid[y][x] = "#"
        if not is_path_possible(grid):
            return f"{x},{y}"

    return "No byte blocks the path."

def main():
    filename = "aoc_day18_part1.txt"
    grid_size = 71  # Adjusted for 0 to 70 inclusive

    byte_positions = parse_input(filename)
    blocking_byte = find_blocking_byte(grid_size, byte_positions)

    print(f"The coordinates of the first byte that blocks the path are: {blocking_byte}")

if __name__ == "__main__":
    main()
