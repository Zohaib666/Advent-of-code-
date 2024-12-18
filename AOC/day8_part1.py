# day8_part1
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

# Function to calculate antinodes for a specific frequency
def calculate_antinodes_for_frequency(positions, map_width, map_height):
    antinodes = set()
    n = len(positions)
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = positions[i]
            x2, y2 = positions[j]
            dx, dy = x2 - x1, y2 - y1

            # Antinode on one side
            p1 = (x1 - dx, y1 - dy)
            if 0 <= p1[0] < map_width and 0 <= p1[1] < map_height:
                antinodes.add(p1)

            # Antinode on the other side
            p2 = (x2 + dx, y2 + dy)
            if 0 <= p2[0] < map_width and 0 <= p2[1] < map_height:
                antinodes.add(p2)
    return antinodes

# Main function to process the map and count unique antinodes
def count_unique_antinodes(file_path):
    antennas, map_width, map_height = parse_map_from_file(file_path)
    unique_antinodes = set()

    for freq, positions in antennas.items():
        unique_antinodes.update(calculate_antinodes_for_frequency(positions, map_width, map_height))

    return len(unique_antinodes)

# Path to your input file
input_file = 'day8_part1.txt'

# Output the total number of unique antinode locations
print(count_unique_antinodes(input_file))
