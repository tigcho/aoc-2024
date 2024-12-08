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
    
    # Group antennas by frequency
    antenna_pos = {}
    for x, y, freq in antennas:
        if freq not in antenna_pos:
            antenna_pos[freq] = []
        antenna_pos[freq].append(complex(x, y))
    
    antinodes = set()
    
    for freq, pos_list in antenna_pos.items():
        for i, pos in enumerate(pos_list[:-1]):
            for pair_pos in pos_list[i+1:]:
                diff = pos - pair_pos
                
                # Check points in both directions from first antenna
                curr_pos = pos + diff
                while 0 <= curr_pos.real < width and 0 <= curr_pos.imag < height:
                    antinodes.add((int(curr_pos.real), int(curr_pos.imag)))
                    curr_pos += diff
                
                curr_pos = pair_pos - diff
                while 0 <= curr_pos.real < width and 0 <= curr_pos.imag < height:
                    antinodes.add((int(curr_pos.real), int(curr_pos.imag)))
                    curr_pos -= diff
        
        if len(pos_list) > 1:
            for pos in pos_list:
                antinodes.add((int(pos.real), int(pos.imag)))
    
    return len(antinodes)

with open("input", "r") as file:
    example_grid = file.read()

result = find_antinodes(example_grid)
print(f"Number of unique antinode locations: {result}")
