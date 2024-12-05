def search_xmas(word):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (-1, 0), (0, -1)]

    def search(x, y, dx, dy):
        return all(
            0 <= x + dx * i < len(grid) and
            0 <= y + dy * i < len(grid[0]) and
            grid[x + dx * i][y + dy * i] == word[i]
            for i in range(len(word))
        )
    
    return sum(
        search(x, y, dx, dy)
        for x in range(len(grid))
        for y in range(len(grid[0]))
        for dx, dy in directions
    )

with open("input", "r") as file:
    grid = [line.strip() for line in file]

print("XMAS appears", search_xmas("XMAS"), "times")

# Part 2
def search_x_mas(grid):
    n = len(grid)
    m = len(grid[0])
    count = 0

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if grid[i][j] == 'A' and all(
                grid[i + dx][j + dy] + grid[i][j] + grid[i - dx][j - dy] in {"MAS", "SAM"}
                for dx, dy in [(1, 1), (1, -1)]
            ):
                count += 1
    return count

with open("input", "r") as file:
    example_grid = [line.strip() for line in file]
print("X-MAS appears", search_x_mas(example_grid), "times")

