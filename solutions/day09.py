import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.aoc_utils import get_input, timer, configure_logging

@timer
def part1(input_lines):
    input_string = input_lines[0].strip()
    data_blocks = ''.join([input_string[i] for i in range(len(input_string)) if i % 2 == 0])
    free_blocks = ''.join([input_string[i] for i in range(len(input_string)) if i % 2 != 0])
    data_blocks_decoded = [str(i) * int(data_blocks[i]) for i in range(len(data_blocks))]
    free_blocks_decoded = ["." * int(free_blocks[i]) for i in range(len(free_blocks))]

    logging.debug(f"Data blocks: {data_blocks}")
    logging.debug(f"Data blocks decoded: {data_blocks_decoded}")
    logging.debug(f"Free blocks: {free_blocks}")
    logging.debug(f"Free blocks decoded: {free_blocks_decoded}")

    joined = join_alternating(data_blocks_decoded, free_blocks_decoded)
    logging.debug(f"Resulting string: {joined}")

    dot_tail = ''
    for char in reversed(joined):
        if char.isdigit():
            joined = joined.replace('.', char, 1)
            joined = joined[:-1]
            dot_tail += '.'
        elif char == '.':
            dot_tail += '.'
            joined = joined[:-1]
        if '.' not in joined:
            break

    res_str = joined + dot_tail

    logging.debug(f"Current string: {res_str}")

    sum = 0
    for i in range(len(res_str)):
        if res_str[i].isdigit():
            sum += int(res_str[i]) * i

    return sum

def join_alternating(data_blocks_decoded, free_blocks_decoded):
    result = []
    min_len = min(len(data_blocks_decoded), len(free_blocks_decoded))
    for i in range(min_len):
        result.append(data_blocks_decoded[i])
        result.append(free_blocks_decoded[i])
    result.extend(data_blocks_decoded[min_len:] + free_blocks_decoded[min_len:])
    return ''.join(result)


@timer
def part2(input_lines):
    # Your Part 2 code
    pass

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
