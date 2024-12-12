def get_neighbors(x, y, rows, cols):
    neighbors = []
    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols:
            neighbors.append((nx, ny))
    return neighbors

def get_region(x, y, grid, visited):
    rows, cols = len(grid), len(grid[0])
    stack = [(x, y)]
    region = set()
    plant_type = grid[x][y]
    perimeter = 0

    while stack:
        curr_x, curr_y = stack.pop()
        if (curr_x, curr_y) in visited:
            continue

        visited.add((curr_x, curr_y))
        region.add((curr_x, curr_y))

        edge_count = 4 
        for nx, ny in get_neighbors(curr_x, curr_y, rows, cols):
            if grid[nx][ny] == plant_type:
                edge_count -= 1 
                if (nx, ny) not in visited:
                    stack.append((nx, ny))

        perimeter += edge_count

    return len(region), perimeter

def total_price(garden_map):
    grid = [list(row.strip()) for row in garden_map.strip().split('\n')]
    rows, cols = len(grid), len(grid[0])
    visited = set()
    total_price = 0

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                area, perimeter = get_region(i, j, grid, visited)
                price = area * perimeter
                total_price += price

    return total_price

with open("input", "r") as f:
    test = f.read()

print(f"Total price: {total_price(test)}")
