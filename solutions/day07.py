import sys
import os
import itertools
import logging
from itertools import product
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.aoc_utils import get_input, timer, configure_logging

def evaluate_expression(nums, ops):
    result = int(nums[0])
    expression = str(nums[0])
    for i in range(len(ops)):
        if ops[i] == '+':
            result += int(nums[i + 1])
        elif ops[i] == '*':
            result *= int(nums[i + 1])
        expression += f" {ops[i]} {nums[i + 1]}"
    return result, expression

def evaluate_expression_with_concat(nums, ops):
    result = int(nums[0])
    expression = str(nums[0])
    for i in range(len(ops)):
        if ops[i] == '+':
            result += int(nums[i + 1])
        elif ops[i] == '*':
            result *= int(nums[i + 1])
        elif ops[i] == '||':
            result = int(str(result) + str(nums[i + 1]))
        expression += f" {ops[i]} {nums[i + 1]}"
    return result, expression

@timer
def part1(input_lines):
    total_sum = 0
    for line in input_lines:
        line = line.strip()
        target_str, numbers_str = line.split(':', 1)
        target = int(target_str.strip())
        nums = list(map(int, numbers_str.strip().split()))
        found = False
        # Use existing numbers without concatenation
        grouping = nums
        num_ops = len(grouping) - 1
        for ops in product('+*', repeat=num_ops):
            result, expression = evaluate_expression(grouping, ops)
            if result == target:
                total_sum += target
                found = True
                break  # Proceed to next line after finding a valid combination
        if found:
            continue  # Move to the next line
    return total_sum

@timer
def part2(input_lines):
    total_sum = 0
    for line in input_lines:
        line = line.strip()
        if not line:
            continue
        key, value = line.split(':')
        target = int(key.strip())
        numbers = value.strip().split()
        numbers = list(map(int, numbers))
        num_ops = len(numbers) - 1
        found = False
        for ops in product(['+', '*', '||'], repeat=num_ops):
            result, expression = evaluate_expression_with_concat(numbers, ops)
            logging.debug(f"Trying expression for {target}: {expression}")
            if result == target:
                total_sum += target
                logging.debug(f"Valid expression for {target}: {expression}")
                found = True
                break  # Proceed to next line after finding a valid combination
        if found:
            continue  # Move to the next line
    return total_sum

if __name__ == "__main__":
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
