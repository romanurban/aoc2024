import sys
import os
import logging
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.aoc_utils import get_input, timer, configure_logging

def mul(a, b):
    try:
        # Try to convert a and b to integers
        a = int(a)
        b = int(b)
        return a * b
    except ValueError:
        # If conversion fails, return 0
        return 0

@timer
def part1(input_lines):
    res = 0
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    
    for line in input_lines:
        line = line.strip()
        matches = mul_pattern.findall(line)
        
        for match in matches:
            a, b = match
            multiplication = mul(a, b)
            res += multiplication
            logging.debug(f"mul({a}, {b}) = {multiplication}")
    
    return res

@timer
def part2(input_lines):
    # Concatenate all lines into a single string
    combined_line = ''.join(input_lines)
    
    # Remove fragments enclosed between "don't(" and "do()"
    while "don't(" in combined_line and "do()" in combined_line:
        start_index = combined_line.index("don't(")
        end_index = combined_line.index("do()", start_index) + len("do()")
        combined_line = combined_line[:start_index] + combined_line[end_index:]
    
    res = 0
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    matches = mul_pattern.findall(combined_line)
    
    for match in matches:
        a, b = match
        multiplication = mul(a, b)
        res += multiplication
        logging.debug(f"mul({a}, {b}) = {multiplication}")
    
    return res

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
