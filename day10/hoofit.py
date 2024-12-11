from typing import List, Tuple

def hoofit(topo: List[str]) -> int:
    def neighbors(x: int, y: int) -> List[Tuple[int, int]]:
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    
    def dfs(x: int, y: int, memo: List[List[int]]) -> int:
        if memo[y][x] != -1:
            return memo[y][x]
        
        if topo[y][x] == '9':
            return 1
        
        count = 0
        for nx, ny in neighbors(x, y):
            if 0 <= nx < len(topo[0]) and 0 <= ny < len(topo):
                if int(topo[ny][nx]) == int(topo[y][x]) + 1:
                    count += dfs(nx, ny, memo)
        
        memo[y][x] = count
        return count

    memo = [[-1 for _ in range(len(topo[0]))] for _ in range(len(topo))]
    ratings = []

    for y in range(len(topo)):
        for x in range(len(topo[0])):
            if topo[y][x] == '0':
                ratings.append(dfs(x, y, memo))

    return sum(ratings)

with open("input", "r") as file:
    topo = file.read().splitlines()

print(hoofit(topo))
