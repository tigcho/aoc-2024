def parse_grid(grid):
    antennas = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell not in ".#":
                antennas.append((x, y, cell))
    return antennas

def find_antinodes(grid):
    grid = [list(row) for row in grid.strip().split("\n")]
    width, height = len(grid[0]), len(grid)
    antennas = parse_grid(grid)
    antinodes = set()

    for i, (x1, y1, freq1) in enumerate(antennas):
        for x2, y2, freq2 in antennas[i + 1:]:
            if freq1 != freq2:
                continue

            dx, dy = x2 - x1, y2 - y1
            x3, y3 = x2 + dx, y2 + dy
            x4, y4 = x1 - dx, y1 - dy

            if 0 <= x3 < width and 0 <= y3 < height:
                antinodes.add((x3, y3))
            if 0 <= x4 < width and 0 <= y4 < height:
                antinodes.add((x4, y4))

    return len(antinodes)

with open("input", "r") as file:
    example_grid = file.read()

result = find_antinodes(example_grid)
print(f"Number of unique antinode locations: {result}")
