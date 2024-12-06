import sys
import os
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.aoc_utils import get_input, timer, configure_logging

def parse_input(input_lines):
    grid = [list(line.strip()) for line in input_lines]
    return grid

def simulate_movement(grid):
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    right_turn = {'^': '>', 'v': '<', '<': '^', '>': 'v'}
    visited = set()
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell in directions:
                direction = cell
                dx, dy = directions[cell]
                x_pos, y_pos = x, y
                break
        else:
            continue
        break

    max_rows = len(grid)
    max_cols = len(grid[0])
    visited.add((x_pos, y_pos))  # Add the initial position to visited
    while True:
        # Check if next position is within bounds and not an obstacle
        next_x, next_y = x_pos + dx, y_pos + dy
        if not (0 <= next_x < max_rows and 0 <= next_y < max_cols):
            break
        if grid[next_x][next_y] == '#':
            # Turn 90 degrees to the right
            direction = right_turn[direction]
            dx, dy = directions[direction]
            continue
        # Move to the next position
        x_pos += dx
        y_pos += dy
        # Mark current position as visited
        visited.add((x_pos, y_pos))

    return visited

@timer
def part1(input_lines):
    grid = parse_input(input_lines)
    visited = simulate_movement(grid)
    logging.debug(f"Visited positions: {visited}")
    return len(visited)

def main():
    sample_mode = '--test' in sys.argv
    input_lines = get_input(day=6, sample=sample_mode)
    configure_logging(debug='--debug' in sys.argv)
    unique_visited_count = part1(input_lines)
    logging.info(f"Unique visited tiles count: {unique_visited_count}")

if __name__ == "__main__":
    main()
