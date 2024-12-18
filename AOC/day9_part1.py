from pathlib import Path

# Define the file path (adjust if necessary)
fn = "day9_part1.txt"

# Read and process the input data
dat = open(fn).read().strip().split("\n")
s = dat[0]

# Initialize variables
files = []
layout = []
file_id = 0

# Build the initial layout based on file sizes and free space
for i, ch in enumerate(s):
    length = int(ch)
    if i % 2 == 0:  # File block (even indices)
        layout.extend([str(file_id)] * length)
        file_id += 1
    else:  # Free space block (odd indices)
        layout.extend(["."] * length)

# Compacting process: move files to the left to fill free space
while True:
    try:
        # Find the first occurrence of free space ('.')
        gap_index = layout.index(".")
    except ValueError:
        # No free space left
        break

    # Check if there are files to the right of the gap
    found_file_to_the_right = any(ch != "." for ch in layout[gap_index + 1:])
    if not found_file_to_the_right:
        break

    # Move the file closest to the gap (from the right) to the gap
    for i in range(len(layout) - 1, -1, -1):
        if layout[i] != ".":
            layout[gap_index], layout[i] = layout[i], "."
            break

# Calculate the checksum: multiply each file position by its file ID
checksum = 0
for i, ch in enumerate(layout):
    if ch != ".":
        checksum += i * int(ch)

# Output the checksum
print(checksum)
