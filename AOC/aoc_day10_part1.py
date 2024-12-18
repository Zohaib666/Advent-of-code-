from collections import deque

def parse_input(file_path):
    """Reads the topographic map from the input file."""
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip())) for line in file]

def find_trailheads(map_data):
    """Finds all positions with height 0."""
    trailheads = []
    for row in range(len(map_data)):
        for col in range(len(map_data[0])):
            if map_data[row][col] == 0:
                trailheads.append((row, col))
    return trailheads

def is_valid_move(map_data, visited, x, y, current_height):
    """Checks if moving to (x, y) is valid."""
    rows, cols = len(map_data), len(map_data[0])
    return (
        0 <= x < rows and 0 <= y < cols and
        not visited[x][y] and
        map_data[x][y] == current_height + 1
    )

def bfs(map_data, start):
    """Performs BFS to find all reachable 9-height positions from the trailhead."""
    rows, cols = len(map_data), len(map_data[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start[0], start[1], 0)])  # (x, y, current_height)
    reachable_nines = set()

    while queue:
        x, y, current_height = queue.popleft()
        visited[x][y] = True

        if map_data[x][y] == 9:
            reachable_nines.add((x, y))

        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid_move(map_data, visited, nx, ny, current_height):
                queue.append((nx, ny, map_data[nx][ny]))

    return len(reachable_nines)

def compute_scores(map_data):
    """Computes the scores for all trailheads and returns their sum."""
    trailheads = find_trailheads(map_data)
    total_score = 0

    for trailhead in trailheads:
        total_score += bfs(map_data, trailhead)

    return total_score

if __name__ == "__main__":
    input_file = "aoc_day10_part1.txt"  # Replace with your input file name
    map_data = parse_input(input_file)
    total_score = compute_scores(map_data)
    print(f"Sum of the scores of all trailheads: {total_score}")
