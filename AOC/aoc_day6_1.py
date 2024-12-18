def read_input(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]

def simulate_guard_movement(map_data):
    directions = ['^', '>', 'v', '<']  # Up, Right, Down, Left
    delta = {
        '^': (-1, 0),  # Up
        '>': (0, 1),   # Right
        'v': (1, 0),   # Down
        '<': (0, -1)   # Left
    }

    rows, cols = len(map_data), len(map_data[0])
    visited = set()

    # Locate guard's initial position and direction
    for r in range(rows):
        for c in range(cols):
            if map_data[r][c] in directions:
                guard_pos = (r, c)
                guard_dir = map_data[r][c]
                map_data[r][c] = '.'  # Replace guard's initial position with empty space
                break

    visited.add(guard_pos)

    while True:
        # Calculate next position
        dr, dc = delta[guard_dir]
        next_pos = (guard_pos[0] + dr, guard_pos[1] + dc)

        # Check if the next position is out of bounds
        if not (0 <= next_pos[0] < rows and 0 <= next_pos[1] < cols):
            break

        # Check for an obstacle
        if map_data[next_pos[0]][next_pos[1]] == '#':
            # Turn right (update direction)
            guard_dir = directions[(directions.index(guard_dir) + 1) % 4]
        else:
            # Move forward
            guard_pos = next_pos
            visited.add(guard_pos)

    return len(visited)

if __name__ == "__main__":
    # Replace 'input.txt' with the path to your input file
    file_path = 'aoc_day6_1.txt'
    map_data = read_input(file_path)
    result = simulate_guard_movement(map_data)
    print(f"Number of distinct positions visited: {result}")
