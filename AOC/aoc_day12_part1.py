#aoc_day12_part1 
from collections import deque

def parse_input(file_path):
    with open(file_path, 'r') as f:
        return [list(line.strip()) for line in f]

def find_regions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    regions = []

    def bfs(start_row, start_col):
        queue = deque([(start_row, start_col)])
        visited[start_row][start_col] = True
        region_cells = []
        region_type = grid[start_row][start_col]

        while queue:
            r, c = queue.popleft()
            region_cells.append((r, c))

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == region_type:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

        return region_cells

    for row in range(rows):
        for col in range(cols):
            if not visited[row][col]:
                regions.append(bfs(row, col))

    return regions

def calculate_area_and_perimeter(region, grid):
    area = len(region)
    perimeter = 0

    for r, c in region:
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == grid[r][c]):
                perimeter += 1

    return area, perimeter

def calculate_total_price(grid):
    regions = find_regions(grid)
    total_price = 0

    for region in regions:
        area, perimeter = calculate_area_and_perimeter(region, grid)
        total_price += area * perimeter

    return total_price

def main():
    input_file = 'aoc_day12_part1.txt'
    grid = parse_input(input_file)
    total_price = calculate_total_price(grid)
    print(f"Total price of fencing all regions: {total_price}")

if __name__ == '__main__':
    main()