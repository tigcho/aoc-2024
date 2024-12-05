from collections import defaultdict

def solve(input):
    with open(input, 'r') as file:
        rules, updates = file.read().strip().split('\n\n')
    
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for rule in rules.split('\n'):
        u, v = map(int, rule.split('|'))  # Each rule is a pair u -> v
        graph[u].append(v)  # Add edge u -> v to the graph
        in_degree[v] += 1
        in_degree[u] += in_degree[u] 
    
    def is_topologically_sorted(update):
        index_map = {page: idx for idx, page in enumerate(update)}
        
        # Check that for every edge u -> v, index of u < index of v
        return all(index_map[u] < index_map[v] for u in update for v in graph[u] if v in index_map)
    
    total_sum = 0
    for upd in updates.split('\n'):
        update = list(map(int, upd.split(','))) 
        
        if is_topologically_sorted(update):
            middle_page = update[len(update) // 2] 
            total_sum += middle_page 
    
    return total_sum

file = 'input' 
print("Sum of middle pages:", solve(file))
