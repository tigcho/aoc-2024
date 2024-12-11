"""

"""
from collections import deque
from typing import List, Tuple

def hoofit(topo: List[str]) -> int:
    def neighbors(x: int, y: int) -> List[Tuple[int, int]]:
        return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    
    def dfs(x: int, y: int) -> int:
        visited = set()
        stack = deque([(x, y)])
        count = 0

        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if topo[y][x] == '9':
                count += 1
            for nx, ny in neighbors(x, y):
                if nx < 0 or nx >= len(topo[0]) or ny < 0 or ny >= len(topo):
                    continue
                if topo[ny][nx] == '.':
                    continue
                if int(topo[ny][nx]) == int(topo[y][x]) + 1:
                    stack.append((nx, ny))

        return count

    score = 0

    for y in range(len(topo)):
        for x in range(len(topo[0])):
            if topo[y][x] == '0':
                score += dfs(x, y)

    return score

with open("input", "r") as file:
    topo = file.read().splitlines()

print(hoofit(topo))



