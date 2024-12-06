from collections import defaultdict, deque

def solve(input):
    with open(input, 'r') as file:
        rules, updates = file.read().strip().split('\n\n')
    
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for rule in rules.split('\n'):
        u, v = map(int, rule.split('|'))  # Each rule is a pair u -> v
        graph[u].append(v)  # Add edge u -> v to the graph
        in_degree[v] += 1
    
    def is_topologically_sorted(update):
        index_map = {page: idx for idx, page in enumerate(update)}
        return all(index_map[u] < index_map[v] for u in update for v in graph[u] if v in index_map)
    
    def topological_sort(pages):
        local_in_degree = defaultdict(int)
        local_graph = defaultdict(list)
        
        # Build local graph with only the pages we care about
        for u in pages:
            for v in graph[u]:
                if v in pages:
                    local_graph[u].append(v)
                    local_in_degree[v] += 1
        
        queue = deque([p for p in pages if local_in_degree[p] == 0])
        result = []
        
        while queue:
            u = queue.popleft()
            result.append(u)
            
            for v in local_graph[u]:
                local_in_degree[v] -= 1
                if local_in_degree[v] == 0:
                    queue.append(v)
        
        return result
    
    # Part 1
    total_sum_part1 = 0
    incorrect_updates = []
    
    for upd in updates.split('\n'):
        update = list(map(int, upd.split(',')))
        
        if is_topologically_sorted(update):
            middle_page = update[len(update) // 2]
            total_sum_part1 += middle_page
        else:
            incorrect_updates.append(update)
    
    # Part 2
    total_sum_part2 = 0
    
    for update in incorrect_updates:
        correct_order = topological_sort(set(update))
        middle_page = correct_order[len(correct_order) // 2]
        total_sum_part2 += middle_page
    
    return total_sum_part1, total_sum_part2

file = 'input'
part1, part2 = solve(file)
print("Part 1 - Sum of middle pages (correct orders):", part1)
print("Part 2 - Sum of middle pages (fixed incorrect orders):", part2)
