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

def find_shortest_path(grid):
    """Finds the shortest path using A* algorithm."""
    grid_size = len(grid)
    start = (0, 0)
    end = (grid_size - 1, grid_size - 1)

    # Priority queue for A*
    pq = []
    heapq.heappush(pq, (0, start))  # (cost, position)

    # Distance dictionary
    distances = {start: 0}

    # Directions for movement
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        current_cost, (x, y) = heapq.heappop(pq)

        if (x, y) == end:
            return current_cost

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, grid):
                new_cost = distances[(x, y)] + 1
                if (nx, ny) not in distances or new_cost < distances[(nx, ny)]:
                    distances[(nx, ny)] = new_cost
                    priority = new_cost + abs(nx - end[0]) + abs(ny - end[1])  # Heuristic (Manhattan distance)
                    heapq.heappush(pq, (priority, (nx, ny)))

    return -1  # If no path is found

def main():
    filename = "aoc_day18_part1.txt"
    grid_size = 71  # Adjusted for 0 to 70 inclusive
    max_bytes = 1024

    byte_positions = parse_input(filename)
    grid = simulate_corruption(grid_size, byte_positions, max_bytes)

    shortest_path = find_shortest_path(grid)

    if shortest_path == -1:
        print("No path found to the exit.")
    else:
        print(f"The minimum number of steps to reach the exit is: {shortest_path}")

if __name__ == "__main__":
    main()
