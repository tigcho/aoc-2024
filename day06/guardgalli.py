def simulate_guard_path(grid):
    grid = [list(row) for row in grid.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    
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

def simulate_with_obstacle(grid, obstacle_pos, start_pos, rows, cols):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_dir = 0
    current_pos = start_pos
    visited_states = set()
    max_steps = rows * cols * 4
    step = 0
    
    while step < max_steps:
        state = (current_pos, current_dir)
        if state in visited_states:
            return True
            
        visited_states.add(state)
        row, col = current_pos
        next_row = row + directions[current_dir][0]
        next_col = col + directions[current_dir][1]
        
        if (next_row < 0 or next_row >= rows or 
            next_col < 0 or next_col >= cols):
            return False
        
        if ((next_row, next_col) == obstacle_pos) or grid[next_row][next_col] == '#':
            current_dir = (current_dir + 1) % 4
        else:
            current_pos = (next_row, next_col)
        
        step += 1
    
    return False

def find_loop_positions(input_map):
    grid = [list(row) for row in input_map.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    
    start_pos = None
    empty_positions = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '^':
                start_pos = (i, j)
            elif grid[i][j] == '.':
                empty_positions.append((i, j))
    
    valid_positions = []
    for pos in empty_positions:
        if simulate_with_obstacle(grid, pos, start_pos, rows, cols):
            valid_positions.append(pos)
    
    return valid_positions

with open('input', 'r') as file:
    input_map = file.read()

result1 = simulate_guard_path(input_map)
print(f"Part 1: The guard visits {result1} distinct positions.")

loop_positions = find_loop_positions(input_map)
print(f"Part 2: There are {len(loop_positions)} positions where an obstacle creates a loop.")
