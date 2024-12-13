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
            
            px = int(prize.split('X=')[1].split(',')[0]) + 10000000000000 
            py = int(prize.split('Y=')[1]) + 10000000000000 
            
            machines.append({
                'A': (ax, ay),
                'B': (bx, by),
                'Prize': (px, py)
            })
            
            f.readline()
    
    return machines

def win_prize(a_x, a_y, b_x, b_y, p_x, p_y):
    # Calculate determinant
    det = a_x * b_y - a_y * b_x
    
    if det == 0:
        return False, None, None
        
    a = (p_x * b_y - p_y * b_x) // det
    b = (a_x * p_y - a_y * p_x) // det
    
    if (a * a_x + b * b_x != p_x) or (a * a_y + b * b_y != p_y) or a < 0 or b < 0:
        return False, None, None
        
    return True, a, b

def calc_tokens(a_presses, b_presses):
    return a_presses * 3 + b_presses

def solve(machines):
    total_tokens = 0
    prizes = 0

    for m in machines:
        a_x, a_y = m['A']
        b_x, b_y = m['B']
        p_x, p_y = m['Prize']

        win, a_presses, b_presses = win_prize(a_x, a_y, b_x, b_y, p_x, p_y)

        if win:
            prizes += 1
            tokens = calc_tokens(a_presses, b_presses)
            total_tokens += tokens

    return prizes, total_tokens

machines = parse_input('input')
result = solve(machines)
print(f"Tokens: {result[1]}")
