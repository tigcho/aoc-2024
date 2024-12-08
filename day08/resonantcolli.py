def find_antennas(grid):
    antennas = {}
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] not in '.#':
                freq = grid[y][x]
                if freq not in antennas:
                    antennas[freq] = []
                antennas[freq].append((x, y))
    return antennas

def is_collinear(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (y2-y1) * (x3-x1) == (y3-y1) * (x2-x1)

def find_antinodes(antenna1, antenna2):
    x1, y1 = antenna1
    x2, y2 = antenna2
    antinodes = set()
    
    dx = x2 - x1
    dy = y2 - y1
    
    # Check points along the line in both directions
    for i in [-2, -1, 1, 2]:  # Multipliers for finding antinodes
        x = x1 + dx * i
        y = y1 + dy * i
        
        if is_collinear(antenna1, antenna2, (x, y)):
            d1 = ((x - x1) ** 2 + (y - y1) ** 2) ** 0.5
            d2 = ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
            
            # Check if distances follow the 2:1 ratio
            if abs(d1 * 2 - d2) < 0.0001 or abs(d2 * 2 - d1) < 0.0001:
                antinodes.add((int(round(x)), int(round(y))))
                
    return antinodes

def solve_antenna_problem(grid):
    # Convert grid string to list of lists
    grid = [list(line.strip()) for line in grid.strip().split('\n')]
    height = len(grid)
    width = len(grid[0])
    
    antennas = find_antennas(grid)
    
    all_antinodes = set()
    
    for freq, positions in antennas.items():
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                antinodes = find_antinodes(positions[i], positions[j])
                
                for x, y in antinodes:
                    if 0 <= x < width and 0 <= y < height:
                        all_antinodes.add((x, y))
    
    return len(all_antinodes)

with open ("input", "r") as file:
    example_grid = file.read()

result = solve_antenna_problem(example_grid)
print(f"Number of unique antinode locations: {result}")
