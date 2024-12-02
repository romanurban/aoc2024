import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.aoc_utils import get_input, timer, configure_logging

@timer
def part1(input_lines):
    valid_level_cnt = 0
    for line in input_lines:
        levels = list(map(int, line.split()))

        # Skip levels with duplicate elements
        if len(levels) != len(set(levels)):
            logging.debug("Duplicate", levels)
            continue

        # Skip levels where the difference between adjacent elements is more than 3
        skip = False
        for i in range(len(levels) - 1):
            if abs(levels[i] - levels[i + 1]) > 3:
                skip = True
                break
        if skip:
            logging.debug("Difference > 3", levels)
            continue
    
        sorted_levels = sorted(levels)
        if levels == sorted_levels:
            logging.debug("Ascending")
        elif levels == sorted_levels[::-1]:
            logging.debug("Descending")
        else:
            logging.debug("Neither")
            continue

        # all checks have passed, current levels are valid
        valid_level_cnt += 1
        logging.debug("Valid:", levels)
    return valid_level_cnt

@timer
def part2(input_lines):
    valid_level_cnt = 0
    for line in input_lines:
        levels = list(map(int, line.split()))

        # First run: check the original levels array
        def is_valid(levels):
            # Skip levels with duplicate elements
            if len(levels) != len(set(levels)):
                logging.debug("Duplicate %s", levels)
                return False

            # Skip levels where the difference between adjacent elements is more than 3
            for i in range(len(levels) - 1):
                if abs(levels[i] - levels[i + 1]) > 3:
                    logging.debug("Difference > 3 %s", levels)
                    return False

            sorted_levels = sorted(levels)
            if levels == sorted_levels:
                logging.debug("Ascending")
            elif levels == sorted_levels[::-1]:
                logging.debug("Descending")
            else:
                logging.debug("Neither")
                return False

            return True

        if is_valid(levels):
            valid_level_cnt += 1
            logging.debug("Valid: %s", levels)
            continue

        # Create new levels array by removing one element at a time
        for i in range(len(levels)):
            new_levels = levels[:i] + levels[i+1:]
            logging.debug("New levels after removing element at index %d: %s", i, new_levels)

            if is_valid(new_levels):
                valid_level_cnt += 1
                logging.debug("Valid: %s", new_levels)
                break  # Stop after finding the first valid new_levels

    return valid_level_cnt

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
