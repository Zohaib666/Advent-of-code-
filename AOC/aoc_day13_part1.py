def parse_input(file_path):
    machines = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 4):
            button_a = lines[i].strip().split(': ')[1]
            button_b = lines[i + 1].strip().split(': ')[1]
            prize = lines[i + 2].strip().split(': ')[1]
            
            a_x, a_y = map(int, button_a.replace('X+', '').replace('Y+', '').split(', '))
            b_x, b_y = map(int, button_b.replace('X+', '').replace('Y+', '').split(', '))
            prize_x, prize_y = map(int, prize.replace('X=', '').replace('Y=', '').split(', '))
            
            machines.append(((a_x, a_y), (b_x, b_y), (prize_x, prize_y)))
    return machines

def min_tokens_for_prize(a, b, prize):
    prize_x, prize_y = prize
    a_x, a_y = a
    b_x, b_y = b
    
    min_tokens = float('inf')
    found_solution = False
    
    for a_count in range(101):  # A button can be pressed 0 to 100 times
        for b_count in range(101):  # B button can be pressed 0 to 100 times
            if a_count * a_x + b_count * b_x == prize_x and a_count * a_y + b_count * b_y == prize_y:
                found_solution = True
                tokens = a_count * 3 + b_count * 1
                min_tokens = min(min_tokens, tokens)
    
    return min_tokens if found_solution else None

def main(file_path):
    machines = parse_input(file_path)
    total_tokens = 0
    total_prizes = 0
    
    for a, b, prize in machines:
        tokens = min_tokens_for_prize(a, b, prize)
        if tokens is not None:
            total_tokens += tokens
            total_prizes += 1
    
    print(f"Total prizes won: {total_prizes}")
    print(f"Minimum tokens spent: {total_tokens}")

if __name__ == "__main__":
    input_file = 'aoc_day13_part1.txt'  # Change this to your input file path
    main(input_file)