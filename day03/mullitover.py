import re

def process_instructions(input_data):
    mul_pattern = re.compile(r'mul\((\d+),\s*(\d+)\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")
    
    mul_enabled = True
    total_sum = 0
    
    i = 0
    while i < len(input_data):
        if do_pattern.match(input_data[i:]):
            mul_enabled = True
            i += len('do()')
        elif dont_pattern.match(input_data[i:]):
            mul_enabled = False
            i += len("don't()")
        else:
            mul_match = mul_pattern.match(input_data[i:])
            if mul_match:
                if mul_enabled: 
                    x, y = map(int, mul_match.groups())
                    total_sum += x * y
                i += len(mul_match.group(0))
            else:
                i += 1
    
    return total_sum

with open("input", "r") as f:
    input_data = f.read()

result = process_instructions(input_data)
print("The sum of the products of enabled multiplications is:", result)
