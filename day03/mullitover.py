import re

def match_regex(expression):
    # regex must match mul(X, Y)
    pattern = re.compile(r'mul\((\d+),\s*(\d+)\)')
    matches = pattern.findall(expression)
    total_sum = sum(int(x) * int(y) for x, y in matches)
    return total_sum

with open("input", "r") as f:
    input_data = f.read()

print("The sum of the products is:", match_regex(input_data))
