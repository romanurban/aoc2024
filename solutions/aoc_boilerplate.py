import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.aoc_utils import get_input, timer

@timer
def part1(input_lines):
    # Your Part 1 code
    pass

@timer
def part2(input_lines):
    # Your Part 2 code
    pass

def main():
    import sys
    sample_mode = '--test' in sys.argv
    timing_enabled = '--time' in sys.argv

    # Set the 'enabled' attribute of the wrapper functions
    part1.enabled = timing_enabled
    part2.enabled = timing_enabled

    input_lines = get_input(sample=sample_mode)
    result1 = part1(input_lines)
    print(f"Part 1 Result: {result1}")

    result2 = part2(input_lines)
    print(f"Part 2 Result: {result2}")

if __name__ == '__main__':
    main()
