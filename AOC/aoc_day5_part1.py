from collections import defaultdict, deque

def parse_input(file_path):
    with open(file_path, 'r') as f:
        sections = f.read().strip().split("\n\n")
    
    rules = [tuple(map(int, line.split('|'))) for line in sections[0].splitlines()]
    updates = [list(map(int, line.split(','))) for line in sections[1].splitlines()]
    
    return rules, updates

def build_graph(rules):
    graph = defaultdict(list)
    for x, y in rules:
        graph[x].append(y)
    return graph

def is_valid_order(update, graph):
    # Create a map of indices for quick lookup
    index_map = {page: i for i, page in enumerate(update)}
    for x, y in graph.items():
        if x in index_map and any(index_map[y_page] <= index_map[x] for y_page in y if y_page in index_map):
            return False
    return True

def get_middle_page(update):
    return update[len(update) // 2]

def calculate_sum(file_path):
    rules, updates = parse_input(file_path)
    graph = build_graph(rules)
    
    valid_updates = []
    for update in updates:
        if is_valid_order(update, graph):
            valid_updates.append(get_middle_page(update))
    
    return sum(valid_updates)

# Example usage
file_path = 'day5_1.txt'  # Replace with the path to your input file
result = calculate_sum(file_path)
print("Sum of middle pages:", result)
