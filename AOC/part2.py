from collections import Counter

# Define the file path (update the path to your actual file location)
file_path = "part2.txt"  # Replace "part.txt" with your actual file path

def calculate_similarity_score(file_path):
    # Read the file and parse data
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please check the path.")
        return None

    # Split lines into two lists
    left_list = []
    right_list = []
    for line in lines:
        # Attempt to parse each line; skip invalid ones
        try:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)
        except ValueError:
            # Print a warning if a line is skipped (optional)
            print(f"Skipped invalid line: {line.strip()}")
    
    # Count occurrences in the right list
    right_count = Counter(right_list)
    
    # Calculate similarity score
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_count.get(num, 0)
    
    return similarity_score

# Execute the function and print the score
if __name__ == "__main__":
    # Prompt for file path (optional, for user input)
    # file_path = input("Enter the path to the file: ")

    score = calculate_similarity_score(file_path)
    if score is not None:
        print(f"Similarity Score: {score}")
    else:
        print("Similarity score calculation could not be completed.")
