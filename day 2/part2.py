def is_safe(report):
    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
    return all(report[i] < report[i + 1] for i in range(len(report) - 1)) or all(report[i] > report[i + 1] for i in range(len(report) - 1))

def is_safe_with_dampener(report):
    for i in range(len(report)):
        new_report = report[:i] + report[i + 1:]
        if is_safe(new_report):
            return True
    return False

def count_safe_reports_with_dampener(file_path):
    safe_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            report = list(map(int, line.split()))
            if is_safe(report) or is_safe_with_dampener(report):
                safe_count += 1

    return safe_count
safe_reports = count_safe_reports_with_dampener("./input.txt")
print(f"Numero di report sicuri con il Problem Dampener: {safe_reports}")
