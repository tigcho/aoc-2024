def next_secret(n):
    n = (n ^ (n * 64)) % 16777216
    n = (n ^ (n // 32)) % 16777216
    n = (n ^ (n * 2048)) % 16777216
    
    return n

with open('input') as f:
    inputs = [int(line.strip()) for line in f]

result = 0
for start in inputs:
    n = start
    for _ in range(2000):
        n = next_secret(n)
    result += n

print(result)
