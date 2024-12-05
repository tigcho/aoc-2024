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
