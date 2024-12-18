# aoc_day11_part1
def process_stones(stones, blinks):
    """
    Processes the stones based on the rules for the given number of blinks.

    Parameters:
        stones (list[int]): Initial list of stones.
        blinks (int): Number of blinks to process.

    Returns:
        int: The total number of stones after processing.
    """
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                new_stones.extend([left, right])
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    return len(stones)

# Example usage:
def main():
    input_file = "input.txt"  # Specify your input file name
    blinks = 25  # Number of blinks for Part One

    with open(input_file, "r") as file:
        initial_stones = [int(x) for x in file.read().strip().split()]

    total_stones = process_stones(initial_stones, blinks)
    print("Number of stones after", blinks, "blinks:", total_stones)

if __name__ == "__main__":
    main()