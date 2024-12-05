import sys
import os
import logging
from functools import cmp_to_key
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.aoc_utils import get_input, timer, configure_logging

def is_valid_page(page, ordering_rules):
    for rule in ordering_rules:
        rule = rule.split('|')
        for i in range(len(page) - 1):
            if str(page[i]) not in rule or str(page[i + 1]) not in rule:
                continue
            x_idx = rule.index(str(page[i]))
            y_idx = rule.index(str(page[i + 1]))
            if x_idx > y_idx:
                return False
    return True

@timer
def part1(ordering_rules, pages):
    sum_of_central_elements = 0
    invalid_pages = []
    for page in pages:
        if is_valid_page(page, ordering_rules):
            central_element = page[len(page) // 2]
            sum_of_central_elements += central_element
            logging.debug(f"Page {page} is valid")
        else:
            invalid_pages.append(page)
            logging.debug(f"Page {page} is invalid")

    return sum_of_central_elements, invalid_pages

@timer
def part2(ordering_rules, invalid_pages):
    def compare_elements(a, b):
        for rule in ordering_rules:
            rule = rule.split('|')
            if str(a) in rule and str(b) in rule:
                x_idx = rule.index(str(a))
                y_idx = rule.index(str(b))
                if x_idx != y_idx:
                    return x_idx - y_idx
        return 0

    sum_of_central_elements = 0
    for page in invalid_pages:
        sorted_page = sorted(page, key=cmp_to_key(compare_elements))
        logging.debug("Sorted page: %s", sorted_page)
        central_element = sorted_page[len(sorted_page) // 2]
        sum_of_central_elements += central_element
        logging.debug(f"Central element of page {sorted_page} is {central_element}")

    return sum_of_central_elements

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

    # Parse the input
    ordering_rules = []
    pages = []
    is_ordering_rules = True

    for line in input_lines:
        if line.strip() == "":
            is_ordering_rules = False
            continue
        if is_ordering_rules:
            ordering_rules.append(line.strip())
        else:
            pages.append(list(map(int, line.strip().split(','))))

    logging.debug(f"Ordering Rules: {ordering_rules}")
    logging.debug(f"Pages: {pages}")

    sum, invalids = part1(ordering_rules, pages)
    logging.info(f"Part 1 Result: {sum}")

    sum2 = part2(ordering_rules, invalids)
    logging.info(f"Part 2 Result: {sum2}")

if __name__ == "__main__":
    main()
