def is_safe(report):
    diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    all_increasing = all(0 < diff <= 3 for diff in diffs)
    all_decreasing = all(-3 <= diff < 0 for diff in diffs)
    return all_increasing or all_decreasing

def count_safe_reports(data):
    safe_count = 0
    for report in data:
        if is_safe(report):
            safe_count += 1
    return safe_count

def analyze_reactor_data(file_path):
    with open(file_path, 'r') as file:
        data = [[int(num) for num in line.split()] for line in file]    
    return count_safe_reports(data)

file_path = '.\input.txt'
safe_reports = analyze_reactor_data(file_path)
print(f"Number of safe reports: {safe_reports}")
