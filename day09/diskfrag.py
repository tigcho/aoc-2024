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

def get_file_spans(blocks):
    # dictionary of file_id: (start_pos, length)
    file_spans = {}
    current_file = None
    start_pos = 0
    length = 0
    
    for i, block in enumerate(blocks):
        if block != '.':
            if current_file is None:
                current_file = block
                start_pos = i
                length = 1
            elif block == current_file:
                length += 1
            else:
                file_spans[current_file] = (start_pos, length)
                current_file = block
                start_pos = i
                length = 1
        elif current_file is not None:
            file_spans[current_file] = (start_pos, length)
            current_file = None
            length = 0
            
    if current_file is not None:
        file_spans[current_file] = (start_pos, length)
        
    return file_spans

def find_leftmost_space_for_file(blocks, file_length):
    count = 0
    start = 0
    
    for i in range(len(blocks)):
        if blocks[i] == '.':
            if count == 0:
                start = i
            count += 1
            if count == file_length:
                return start
        else:
            count = 0
            
    return -1

def compact_disk(blocks):
    blocks = blocks.copy()
    file_spans = get_file_spans(blocks)
    
    # process files in descending order of file ID
    for file_id in sorted(file_spans.keys(), reverse=True):
        start_pos, length = file_spans[file_id]
        new_pos = find_leftmost_space_for_file(blocks, length)
        # if we found a valid pos to move the file and its to the left
        if new_pos != -1 and new_pos < start_pos:
            # clear the old position
            for i in range(start_pos, start_pos + length):
                blocks[i] = '.'
            for i in range(new_pos, new_pos + length):
                blocks[i] = file_id
    
    return blocks

def calculate_checksum(disk_map):
    blocks = expand_disk_map(disk_map)
    blocks = compact_disk(blocks)
    
    checksum = 0
    for pos, block in enumerate(blocks):
        if block != '.':
            checksum += pos * block
    
    return checksum

with open("input", "r") as file:
    test = file.read().strip()

print(calculate_checksum(test))
