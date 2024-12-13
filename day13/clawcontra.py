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


def win_prize(a_x, a_y, b_x, b_y, p_x, p_y, max_presses=100):
    for a in range(max_presses + 1):
        for b in range(max_presses + 1):
            x = a * a_x + b * b_x
            y = a * a_y + b * b_y
            if x == p_x and y == p_y:
                return True, a, b
    return False, None, None

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
