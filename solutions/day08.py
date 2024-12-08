import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.aoc_utils import get_input, timer, configure_logging

@timer
def part1(input_lines):
    grid = [list(line) for line in input_lines]
    antennas = {}

    # Identify the positions and frequencies of antennas
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char.isalnum():  # Check if it is a letter or digit
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))

    def calculate_antinodes(p1, p2):
        antinodes = []
        x1, y1 = p1
        x2, y2 = p2

        # Direction vector from p1 to p2
        dx = x2 - x1
        dy = y2 - y1

        # Antinode positions
        # First antinode (extend the line from p1 away from p2)
        a1_x = x1 - dx
        a1_y = y1 - dy

        # Second antinode (extend the line from p2 away from p1)
        a2_x = x2 + dx
        a2_y = y2 + dy

        antinodes.append((a1_x, a1_y))
        antinodes.append((a2_x, a2_y))

        logging.debug(f"Antinodes for {p1} and {p2}: {antinodes}")
        return antinodes

    # Use a set to track all antinode positions (duplicates will be removed)
    antinode_positions = set()

    # Process each frequency group
    for freq, positions in antennas.items():
        n = len(positions)
        # Check all pairs of antennas with the same frequency
        for i in range(n):
            for j in range(i + 1, n):
                p1, p2 = positions[i], positions[j]
                antinodes = calculate_antinodes(p1, p2)
                for ax, ay in antinodes:
                    # Ensure antinode positions are integers and within grid bounds
                    if ax % 1 == 0 and ay % 1 == 0:
                        ax, ay = int(ax), int(ay)
                        if 0 <= ay < len(grid) and 0 <= ax < len(grid[0]):
                            antinode_positions.add((ax, ay))

    # Total count of unique antinodes
    total_antinodes = len(antinode_positions)
    logging.debug(f"Total unique antinode positions: {total_antinodes}")

    return total_antinodes

@timer
def part2(input_lines):
    import math

    grid = [list(line.rstrip()) for line in input_lines]
    antennas = {}

    # Identify the positions and frequencies of antennas
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char.isalnum():  # Check if it is a letter or digit
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((x, y))

    antinode_positions = set()
    max_x = len(grid[0]) - 1
    max_y = len(grid) - 1

    for freq, positions in antennas.items():
        n = len(positions)
        if n < 2:
            continue  # Skip frequencies with only one antenna

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                dx = x2 - x1
                dy = y2 - y1

                # Calculate GCD to get minimal steps
                gcd = math.gcd(dx, dy)
                step_x = dx // gcd
                step_y = dy // gcd

                # Step in the negative direction
                k = 0
                x, y = x1 - step_x * k, y1 - step_y * k
                while 0 <= x <= max_x and 0 <= y <= max_y:
                    if (x, y) not in antinode_positions:
                        antinode_positions.add((x, y))
                    k += 1
                    x = x1 - step_x * k
                    y = y1 - step_y * k

                # Step in the positive direction
                k = 1
                x, y = x1 + step_x * k, y1 + step_y * k
                while 0 <= x <= max_x and 0 <= y <= max_y:
                    if (x, y) not in antinode_positions:
                        antinode_positions.add((x, y))
                    k += 1
                    x = x1 + step_x * k
                    y = y1 + step_y * k

    total_antinodes = len(antinode_positions)
    return total_antinodes

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
