import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.aoc_utils import get_input, timer, configure_logging

@timer
def part1(input_lines):
    # Your Part 1 code
    pass

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
