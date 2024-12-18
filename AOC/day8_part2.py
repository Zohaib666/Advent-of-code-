# Function to parse the input map file
def parse_map_from_file(file_path):
    with open(file_path, 'r') as file:
        puzzle_map = file.read().splitlines()
    antennas = {}
    for y, row in enumerate(puzzle_map):
        for x, char in enumerate(row):
            if char.isalnum():  # Check if the character is an antenna (letter or digit)
                antennas.setdefault(char, []).append((x, y))
    return antennas, len(puzzle_map[0]), len(puzzle_map)

# Function to calculate all collinear points for a specific frequency
def calculate_collinear_antinodes(positions, map_width, map_height):
    antinodes = set(positions)  # Include antenna positions as antinodes
    n = len(positions)
    for i in range(n):
        for j in range(n):
            if i != j:
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                dx, dy = x2 - x1, y2 - y1

                # Generate points in both directions along the line
                k = 1
                while True:
                    p1 = (x1 - k * dx, y1 - k * dy)
                    p2 = (x2 + k * dx, y2 + k * dy)
                    added = False
                    if 0 <= p1[0] < map_width and 0 <= p1[1] < map_height:
                        antinodes.add(p1)
                        added = True
                    if 0 <= p2[0] < map_width and 0 <= p2[1] < map_height:
                        antinodes.add(p2)
                        added = True
                    if not added:
                        break
                    k += 1
    return antinodes

# Main function to process the map and count unique antinodes
def count_unique_antinodes_with_harmonics(file_path):
    antennas, map_width, map_height = parse_map_from_file(file_path)
    unique_antinodes = set()

    for freq, positions in antennas.items():
        if len(positions) > 1:  # Only calculate for frequencies with more than one antenna
            unique_antinodes.update(calculate_collinear_antinodes(positions, map_width, map_height))

    return len(unique_antinodes)

# Path to your input file
input_file = 'day8_part2.txt'

# Output the total number of unique antinode locations
print(count_unique_antinodes_with_harmonics(input_file))
