from pulp import *
import re

def parse_input(filename):
    machines = []
    
    with open(filename) as f:
        while True:
            a = f.readline().strip()
            if not a:  
                break
            b = f.readline().strip()
            prize = f.readline().strip()
            
            ax = int(a.split('X+')[1].split(',')[0])
            ay = int(a.split('Y+')[1])
            
            bx = int(b.split('X+')[1].split(',')[0])
            by = int(b.split('Y+')[1])
            
            px = int(prize.split('X=')[1].split(',')[0])
            py = int(prize.split('Y=')[1])
            
            machines.append({
                'A': (ax, ay),
                'B': (bx, by),
                'Prize': (px, py)
            })
            
            f.readline()
    
    return machines

def solve_with_pulp(machine):
    a_x, a_y = machine['A']
    b_x, b_y = machine['B']
    p_x, p_y = machine['Prize']
    
    prob = LpProblem("Machine_Puzzle", LpMinimize)
    
    a_presses = LpVariable("button_a", 0, None, LpInteger)
    b_presses = LpVariable("button_b", 0, None, LpInteger)
    
    prob += 3 * a_presses + b_presses
    
    prob += a_x * a_presses + b_x * b_presses == p_x
    prob += a_y * a_presses + b_y * b_presses == p_y
    
    prob.solve(PULP_CBC_CMD(msg=False))
    
    if LpStatus[prob.status] == 'Optimal':
        return True, int(value(a_presses)), int(value(b_presses))
    return False, None, None

def calc_tokens(a_presses, b_presses):
    return a_presses * 3 + b_presses

def solve(machines):
    total_tokens = 0
    prizes = 0
    
    for m in machines:
        win, a_presses, b_presses = solve_with_pulp(m)
        
        if win:
            prizes += 1
            tokens = calc_tokens(a_presses, b_presses)
            total_tokens += tokens
            
    return prizes, total_tokens

machines = parse_input('input')
result = solve(machines)
print(f"Tokens: {result[1]}")
