def solve(data):
    graph = {}
    for line in data.strip().split('\n'):
        a, b = line.split('-')
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
    
    nodes = list(graph.keys())
    count = 0
    
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if nodes[j] in graph[nodes[i]]:  # if connected
                for k in range(j + 1, len(nodes)):
                    if (nodes[k] in graph[nodes[i]] and 
                        nodes[k] in graph[nodes[j]] and
                        any(n.startswith('t') for n in (nodes[i], nodes[j], nodes[k]))):
                        count += 1
    
    return count

with open("input", 'r') as f:
    test_input = f.read()

print(solve(test_input))  
