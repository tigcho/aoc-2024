def simulate_guard_path(grid):
    grid = [list(row) for row in grid.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    
    # Find starting position 
    start_pos = None
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                start_pos = (i, j)
                break
        if start_pos:
            break
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_dir = 0  
    
    visited = set()
    current_pos = start_pos
    visited.add(current_pos)
    
    while True:
        row, col = current_pos
        
        next_row = row + directions[current_dir][0]
        next_col = col + directions[current_dir][1]
        
        if (next_row < 0 or next_row >= rows or 
            next_col < 0 or next_col >= cols):
            break
        
        if grid[next_row][next_col] == '#':
            current_dir = (current_dir + 1) % 4
        else:
            current_pos = (next_row, next_col)
            visited.add(current_pos)
    
    return len(visited)

with open('input', 'r') as file:
    input_map = file.read()

result = simulate_guard_path(input_map)
print(f"The guard visits {result} distinct positions.")
