def parse_input(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    
    registers = [int(line.split(': ')[1]) for line in lines[:3]]
    
    program = [int(x) for x in next(line for line in lines if 'Program:' in line).split('Program:')[1].strip().split(',')]
    
    return program, *registers  

def execute_program(program, *regs):
    registers = list(regs)  
    output = []
    i = 0
    
    while i < len(program) - 1:
        op, val = program[i:i+2]
        
        def get_val(v): return v if v < 4 else registers[v-4] if v < 7 else 0
        
        match op:
            case 0: registers[0] = registers[0] // (2 ** get_val(val))  # adv
            case 1: registers[1] ^= val                                 # bxl
            case 2: registers[1] = get_val(val) % 8                     # bst
            case 3:                                                     # jnz
                if registers[0]: 
                    i = val
                    continue
            case 4: registers[1] ^= registers[2]                        # bxc
            case 5: output.append(str(get_val(val) % 8))                # out
            case 6: registers[1] = registers[0] // (2 ** get_val(val))  # bdv
            case 7: registers[2] = registers[0] // (2 ** get_val(val))  # cdv
        
        i += 2
    
    result = ', '.join(output)
    return result

print(execute_program(*parse_input('input')))
