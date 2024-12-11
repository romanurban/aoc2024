import sys
import os
import logging
from collections import Counter
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.aoc_utils import get_input, timer, configure_logging

@timer
def part1(input_lines):
    stones = [int(x) for x in input_lines[0].split()]
    stone_counts = Counter(stones)
    for _ in range(25):
        new_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                # Rule 1
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                # Rule 2
                digits = str(stone)
                mid = len(digits) // 2
                left = int(digits[:mid].lstrip('0') or '0')
                right = int(digits[mid:].lstrip('0') or '0')
                new_counts[left] += count
                new_counts[right] += count
            else:
                # Rule 3
                new_stone = stone * 2024
                new_counts[new_stone] += count
        stone_counts = new_counts
    total_stones = sum(stone_counts.values())
    return total_stones

@timer
def part2(input_lines):
    stones = [int(x) for x in input_lines[0].split()]
    stone_counts = Counter(stones)
    for _ in range(75):
        new_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                # Rule 1
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                # Rule 2
                digits = str(stone)
                mid = len(digits) // 2
                left = int(digits[:mid].lstrip('0') or '0')
                right = int(digits[mid:].lstrip('0') or '0')
                new_counts[left] += count
                new_counts[right] += count
            else:
                # Rule 3
                new_stone = stone * 2024
                new_counts[new_stone] += count
        stone_counts = new_counts
    total_stones = sum(stone_counts.values())
    return total_stones

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
