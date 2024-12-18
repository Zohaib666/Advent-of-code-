import heapq

def parse_input(file_path):
    """Parses the input file and returns the maze as a 2D list."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if not lines:
            raise ValueError("Input file is empty.")
        maze = [list(line.strip()) for line in lines]
    return maze

def find_position(maze, char):
    """Finds the position of a given character in the maze."""
    for r, row in enumerate(maze):
        for c, cell in enumerate(row):
            if cell == char:
                print(f"Found '{char}' at position: ({r}, {c})")
                return r, c
    print(f"Character '{char}' not found in maze.")
    return None

def a_star(maze, start, end):
    """Implements the A* algorithm to find the lowest score path and track all tiles on best paths."""
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    direction_cost = 1000
    move_cost = 1

    def heuristic(pos):
        """Heuristic function: Manhattan distance."""
        return abs(pos[0] - end[0]) + abs(pos[1] - end[1])

    rows, cols = len(maze), len(maze[0])
    visited = set()
    best_paths = set()
    pq = []  # Priority queue: (score, (row, col), direction)

    start_direction = 0  # Assume starting facing East (index 0)
    heapq.heappush(pq, (0, start, start_direction))

    min_score = float('inf')

    while pq:
        score, (r, c), direction = heapq.heappop(pq)

        if score > min_score:
            continue

        if (r, c) == end:
            min_score = min(min_score, score)
            best_paths.add((r, c))
            continue

        if (r, c, direction) in visited:
            continue
        visited.add((r, c, direction))

        best_paths.add((r, c))

        # Try moving in all 4 directions
        for new_dir, (dr, dc) in enumerate(directions):
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#':
                new_score = score + move_cost

                # Add turning cost if changing direction
                if new_dir != direction:
                    new_score += direction_cost

                heapq.heappush(pq, (new_score, (nr, nc), new_dir))

    return min_score, best_paths

def mark_best_paths(maze, best_paths):
    """Marks all tiles that are part of the best paths on the maze."""
    for r, c in best_paths:
        if maze[r][c] not in ('S', 'E'):
            maze[r][c] = 'O'

def print_maze(maze):
    """Prints the maze."""
    for row in maze:
        print(''.join(row))

def main(input_file):
    maze = parse_input(input_file)
    print("Parsed Maze:")
    print_maze(maze)

    start = find_position(maze, 'S')
    end = find_position(maze, 'E')

    if start is None or end is None:
        raise ValueError("Maze must contain 'S' (start) and 'E' (end) tiles.")

    lowest_score, best_paths = a_star(maze, start, end)
    mark_best_paths(maze, best_paths)

    print("\nLowest score to navigate the maze:", lowest_score)
    print("\nTiles part of the best paths:")
    print_maze(maze)

# Usage example:
# Save your maze input in a file named "input.txt"
# Call main("input.txt")


if __name__ == "__main__":
    input_file = "aoc_day16_part1.txt"  # Replace with your input file name
    main(input_file)
