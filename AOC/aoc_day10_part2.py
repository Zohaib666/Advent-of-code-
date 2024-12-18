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

def dfs(map_data, x, y, current_height):
    """Performs DFS to find all distinct hiking trails from a trailhead."""
    rows, cols = len(map_data), len(map_data[0])
    stack = [(x, y, current_height, set())]  # (x, y, current_height, path)
    distinct_trails = set()

    while stack:
        cx, cy, cheight, path = stack.pop()
        path = path | {(cx, cy)}  # Add current position to path

        if map_data[cx][cy] == 9:
            distinct_trails.add(tuple(sorted(path)))
            continue

        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if (
                0 <= nx < rows and
                0 <= ny < cols and
                (nx, ny) not in path and
                map_data[nx][ny] == cheight + 1
            ):
                stack.append((nx, ny, map_data[nx][ny], path))

    return len(distinct_trails)

def compute_ratings(map_data):
    """Computes the ratings for all trailheads and returns their sum."""
    trailheads = find_trailheads(map_data)
    total_rating = 0

    for trailhead in trailheads:
        total_rating += dfs(map_data, trailhead[0], trailhead[1], 0)

    return total_rating

if __name__ == "__main__":
    input_file = "aoc_day10_part2.txt"  # Replace with your input file name
    map_data = parse_input(input_file)
    total_rating = compute_ratings(map_data)
    print(f"Sum of the ratings of all trailheads: {total_rating}")
