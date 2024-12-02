def is_safe_dampener(report):
    def is_safe(report):
        diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]
        return all(1 <= diff <= 3 for diff in diffs) or all(-3 <= diff <= -1 for diff in diffs)
    
    if is_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if is_safe(modified_report):
            return True

    return False

def count_safe_reports_dampener(filename):
    safe_count = 0
    with open(filename, 'r') as f:
        for line in f:
            report = list(map(int, line.split()))
            if is_safe_dampener(report):
                safe_count += 1
    return safe_count

filename = 'input'
safe_reports = count_safe_reports_dampener(filename)
print(f"Number of safe reports: {safe_reports}")
