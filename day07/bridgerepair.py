def evaluate(nums, ops):
    result = nums[0]
    i = 0
    while i < len(ops):
        if ops[i] == '||':
            result = int(str(result) + str(nums[i + 1]))
        elif ops[i] == '+':
            result += nums[i + 1]
        else:  # '*'
            result *= nums[i + 1]
        i += 1
    return result

def can_make_value_part1(nums, target):
    for i in range(1 << (len(nums) - 1)):
        ops = []
        for j in range(len(nums) - 1):
            if i & (1 << j):
                ops.append('+')
            else:
                ops.append('*')
        if evaluate(nums, ops) == target:
            return True
    return False

def can_make_value_part2(nums, target):
    n = len(nums) - 1
    for i in range(3 ** n):
        ops = []
        temp = i
        for _ in range(n):
            op_type = temp % 3
            if op_type == 0:
                ops.append('+')
            elif op_type == 1:
                ops.append('*')
            else:
                ops.append('||')
            temp //= 3
        
        if evaluate(nums, ops) == target:
            return True
    return False

def solve_calibration(input_data):
    total_part1 = 0
    total_part2 = 0
    
    lines = [line.strip() for line in input_data.split('\n') if line.strip()]
    
    for line in lines:
        nums = list(map(int, line.split(':')[1].split()))
        target = int(line.split(':')[0])
        
        if can_make_value_part1(nums, target):
            total_part1 += target
            
        if can_make_value_part2(nums, target):
            total_part2 += target
    
    return total_part1, total_part2

with open("input", "r") as file:
    puzzle_input = file.read()

part1, part2 = solve_calibration(puzzle_input)
print("Part 1 (only + and *): ", part1)
print("Part 2 (with ||): ", part2)
