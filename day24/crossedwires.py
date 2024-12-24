def solve(f):
    lines = [line for line in f.read().splitlines() if line]
    
    wires = {}
    for line in lines:
        if ':' in line:
            name, value = line.split(': ')
            wires[name] = int(value)
    
    gates = [line for line in lines if '->' in line]
    
    def logic_gate(op, a, b):
        if op == 'AND': return a & b
        if op == 'OR': return a | b
        if op == 'XOR': return a ^ b
    
    while True:
        z_count = len([g for g in gates if '-> z' in g])
        if all(f'z{i:02d}' in wires for i in range(z_count)):
            break
            
        for gate in gates:
            inputs, output = gate.split(' -> ')
            parts = inputs.split()
            
            if output in wires:
                continue
            if not all(x in wires for x in parts if x not in ['AND', 'OR', 'XOR']):
                continue
            
            if len(parts) == 1:  
                wires[output] = wires[parts[0]]
            else:  
                a, op, b = parts
                wires[output] = logic_gate(op, wires[a], wires[b])
    
    result = 0
    z_count = len([g for g in gates if '-> z' in g])
    for i in range(z_count):
        if wires[f'z{i:02d}']:  
            result += (1 << i)  
    
    return result

with open('input') as f:
    print(solve(f))
