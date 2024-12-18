def count_safe_reports_from_file(file_path):
    def is_safe(report):
        differences = [report[i + 1] - report[i] for i in range(len(report) - 1)]
        
        if all(1 <= diff <= 3 for diff in differences):  
            return True
        if all(-3 <= diff <= -1 for diff in differences):  
            return True
        
        return False

    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.strip().split()))
            if is_safe(report):
                safe_count += 1

    return safe_count

file_path = 'data.txt'

safe_count = count_safe_reports_from_file(file_path)
print(f"Safe reports count: {safe_count}")
