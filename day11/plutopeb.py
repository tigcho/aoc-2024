from collections import Counter, defaultdict

def process_stone(num):
    if num == 0:
        return [1]
    
    num_str = str(num)
    if len(num_str) % 2 == 0:
        mid = len(num_str) // 2
        left = int(num_str[:mid])
        right = int(num_str[mid:])
        return [left, right]
    
    return [num * 2024]

def count_stones_after_blinks(n, blinks):
    stones = Counter(map(int, n.split()))
    
    for step in range(blinks):
        new_stones = defaultdict(int)
        for num, count in stones.items():
            results = process_stone(num)
            for result in results:
                new_stones[result] += count
        stones = new_stones

    return sum(stones.values())

with open("input", "r") as file:
    result = file.read().strip()

result1 = count_stones_after_blinks(result, 25)
result2 = count_stones_after_blinks(result, 75)
print("Result for blinking 25 times:", result1)
print("Result for blinking 75 times:", result2)
