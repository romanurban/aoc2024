import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.aoc_utils import get_input, timer, configure_logging

@timer
def part1(input_lines):
    xmas_count = 0
    for line in input_lines:
        xmas_count += line.count('XMAS')
        xmas_count += line.count('SAMX')

    # Transpose the lines to create new lines from vertical columns
    transposed_lines = []
    for i in range(len(input_lines[0])):
        new_line = ''
        for line in input_lines:
            if i < len(line):
                new_line += line[i]
        transposed_lines.append(new_line)

    for line in transposed_lines:
        xmas_count += line.count('XMAS')
        xmas_count += line.count('SAMX')

    # Get all diagonals from top-left to bottom-right
    diagonals = []
    for i in range(len(input_lines)):
        diagonal = ''
        for j in range(len(input_lines)):
            if i + j < len(input_lines) and j < len(input_lines[i + j]):
                diagonal += input_lines[i + j][j]
        diagonals.append(diagonal)

    for i in range(1, len(input_lines[0])):
        diagonal = ''
        for j in range(len(input_lines)):
            if i + j < len(input_lines[0]) and j < len(input_lines):
                diagonal += input_lines[j][i + j]
        diagonals.append(diagonal)

    # Get all diagonals from top-right to bottom-left
    for i in range(len(input_lines)):
        diagonal = ''
        for j in range(len(input_lines)):
            if i + j < len(input_lines) and len(input_lines[i + j]) - 1 - j >= 0:
                diagonal += input_lines[i + j][len(input_lines[i + j]) - 1 - j]
        diagonals.append(diagonal)

    for i in range(1, len(input_lines[0])):
        diagonal = ''
        for j in range(len(input_lines)):
            if i + j < len(input_lines[0]) and len(input_lines[j]) - 1 - (i + j) >= 0:
                diagonal += input_lines[j][len(input_lines[j]) - 1 - (i + j)]
        diagonals.append(diagonal)

    for line in diagonals:
        xmas_count += line.count('XMAS')
        xmas_count += line.count('SAMX')

    return xmas_count

@timer
def part2(input_lines):
    square_count = 0
    rows = len(input_lines)
    cols = len(input_lines[0])
    counted_positions = set()

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if (i, j) not in counted_positions and input_lines[i][j] == 'A':
                if ((input_lines[i-1][j-1] == 'S' and input_lines[i+1][j+1] == 'M') or
                    (input_lines[i-1][j-1] == 'M' and input_lines[i+1][j+1] == 'S')) and \
                   ((input_lines[i-1][j+1] == 'S' and input_lines[i+1][j-1] == 'M') or
                    (input_lines[i-1][j+1] == 'M' and input_lines[i+1][j-1] == 'S')):
                    square_count += 1
                    counted_positions.add((i, j))

    return square_count

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
