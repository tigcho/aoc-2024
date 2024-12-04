import re

def find_xmas(grid):
    n = len(grid)
    
    rows = grid
    columns = [''.join([grid[i][j] for i in range(n)]) for j in range(n)]

    def get_diagonals(grid):
        diagonals = []
        for start in range(-n + 1, n):
            diagonals.append(''.join([grid[i][i - start] for i in range(max(0, start), min(n, n + start))]))
        for start in range(2 * n - 1):
            diagonals.append(''.join([grid[i][start - i] for i in range(max(0, start - n + 1), min(n, start + 1))]))
        return diagonals
    
    diagonals = get_diagonals(grid)
    
    word = "XMAS"
    
    pattern = re.compile(word)
    reverse_pattern = re.compile(word[::-1])
    
    count = 0
    for line in rows + columns + diagonals:
        count += len(pattern.findall(line))
        count += len(reverse_pattern.findall(line))
    
    return count

with open("input") as file:
    input_data = file.read().splitlines()

result = find_xmas(input_data)
print(f"XMAS appears {result} times.")
