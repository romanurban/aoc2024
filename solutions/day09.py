import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.aoc_utils import get_input, timer, configure_logging

@timer
def part1(input_lines):
    input_string = input_lines[0].strip()
    data_blocks = [int(input_string[i]) for i in range(0, len(input_string), 2)]
    free_blocks = [int(input_string[i]) for i in range(1, len(input_string), 2)]

    # Build initial disk representation with correct file IDs
    disk = []
    file_id = 0
    num_files = len(data_blocks)
    for idx in range(num_files):
        data_size = data_blocks[idx]
        disk.extend([file_id] * data_size)
        if idx < len(free_blocks):
            free_size = free_blocks[idx]
            disk.extend([-1] * free_size)
        file_id += 1

    # Compact the disk
    first_free = 0
    last_block = len(disk) - 1
    while first_free < last_block:
        # Find the first free space from the left
        while first_free < last_block and disk[first_free] != -1:
            first_free += 1
        # Find the last file block from the right
        while last_block > first_free and disk[last_block] == -1:
            last_block -= 1
        if first_free < last_block:
            # Move the file block to the free space
            disk[first_free] = disk[last_block]
            disk[last_block] = -1
            first_free += 1
            last_block -= 1

    # Calculate checksum
    checksum = sum(i * disk[i] for i in range(len(disk)) if disk[i] != -1)
    return checksum

@timer
def part2(input_lines):
    input_string = input_lines[0].strip()
    data_blocks = [int(input_string[i]) for i in range(0, len(input_string), 2)]
    free_blocks = [int(input_string[i]) for i in range(1, len(input_string), 2)]

    # Build initial disk representation with file IDs and free spaces
    disk = []
    file_positions = {}  # Track start positions and sizes of files
    file_id = 0
    idx = 0
    for data_size, free_size in zip(data_blocks, free_blocks):
        disk.extend([file_id] * data_size)
        file_positions[file_id] = (idx, data_size)  # (start_index, size)
        idx += data_size
        disk.extend([-1] * free_size)
        idx += free_size
        file_id += 1

    # Handle any remaining data blocks
    for data_size in data_blocks[len(free_blocks):]:
        disk.extend([file_id] * data_size)
        file_positions[file_id] = (idx, data_size)
        idx += data_size
        file_id += 1

    # Move files in decreasing order of file ID
    for fid in range(file_id - 1, -1, -1):
        start_idx, size = file_positions[fid]
        # Find leftmost suitable free space before the file
        left_space_start = None
        left_space_length = 0
        temp_length = 0
        temp_start = None

        for i in range(start_idx):
            if disk[i] == -1:
                if temp_start is None:
                    temp_start = i
                temp_length += 1
                if temp_length >= size:
                    left_space_start = temp_start
                    break
            else:
                temp_length = 0
                temp_start = None

        if left_space_start is not None:
            # Move the file to the leftmost suitable free space
            for i in range(size):
                disk[left_space_start + i] = fid
                disk[start_idx + i] = -1
            # Update file's new position
            file_positions[fid] = (left_space_start, size)

    # Calculate checksum
    checksum = sum(i * disk[i] for i in range(len(disk)) if disk[i] != -1)
    return checksum

def main():
    sample_mode = '--test' in sys.argv
    timing_enabled = '--time' in sys.argv
    debug_mode = '--debug' in sys.argv

    # Configure logging
    configure_logging(debug=debug_mode)

    # Set the 'enabled' attribute of the wrapper functions
    part1.enabled = timing_enabled
    part2.enabled = timing_enabled

    input_lines = get_input(sample=sample_mode)
    result1 = part1(input_lines)
    logging.info(f"Part 1 Result: {result1}")

    result2 = part2(input_lines)
    logging.info(f"Part 2 Result: {result2}")

if __name__ == "__main__":
    main()
