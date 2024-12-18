def process_stones(stones, blinks):
    for blink in range(blinks):
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
        print(f"After blink {blink + 1}, number of stones: {len(stones)}")  # Debug
    return stones

# Example usage:
def main():
    input_file = "aoc_day111_part2.txt"  # Specify your input file name
    blinks = 75  # Number of blinks for Part Two

    with open(input_file, "r") as file:
        initial_stones = [int(x) for x in file.read().strip().split()]

    final_stones = process_stones(initial_stones, blinks)
    print("Number of stones after", blinks, "blinks:", len(final_stones))

if __name__ == "__main__":
    main()
