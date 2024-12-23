from itertools import combinations

def solve(data):
    graph = {}
    for line in data.strip().split('\n'):
        a, b = line.split('-')
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
    
    max_clique = set()
    
    def find_clique(candidates, current_clique):
        nonlocal max_clique
        if len(current_clique) > len(max_clique):
            max_clique = current_clique.copy()
        
        potential = {n for n in candidates 
                    if all(n in graph[v] for v in current_clique)}
        
        for node in potential:
            new_candidates = {n for n in candidates if n > node}  
            find_clique(new_candidates, current_clique | {node})
    
    nodes = sorted(graph.keys())
    find_clique(set(nodes), set())
    
    return ','.join(sorted(max_clique))

with open("input", 'r') as f:
    test_input = f.read()

print(solve(test_input))
