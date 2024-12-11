def expand_disk_map(disk_map):
    blocks = []
    file_id = 0
    
    for i in range(len(disk_map)):
        length = int(disk_map[i])
        if i % 2 == 0:  # file blocks
            blocks.extend([file_id] * length)
            file_id += 1
        else:  # free space
            blocks.extend(['.'] * length)
    
    return blocks

def find_leftmost_space(blocks):
    for i in range(len(blocks)):
        if blocks[i] == '.':
            return i
    return -1

def find_rightmost_file(blocks):
    for i in range(len(blocks)-1, -1, -1):
        if blocks[i] != '.':
            return i
    return -1

def compact_disk(blocks):
    blocks = blocks.copy()
    
    while True:
        left_space = find_leftmost_space(blocks)
        if left_space == -1:
            break
            
        right_file = find_rightmost_file(blocks)
        if right_file <= left_space:
            break
            
        blocks[left_space] = blocks[right_file]
        blocks[right_file] = '.'
    
    return blocks

def calculate_checksum(disk_map):
    blocks = expand_disk_map(disk_map)
    blocks = compact_disk(blocks)
    
    checksum = 0
    for pos, block in enumerate(blocks):
        if block != '.':
            checksum += pos * block
    
    return checksum

with open ("input", "r") as file:
    test = file.read().strip()

print(calculate_checksum(test))
