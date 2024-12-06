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

    # Find initial position and direction
    x_pos, y_pos, direction = None, None, None
    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell in directions:
                direction = cell
                dx, dy = directions[cell]
                x_pos, y_pos = x, y
                break
        if direction is not None:
            break

    max_rows = len(grid)
    max_cols = len(grid[0])
    
    # Track visited states: (x_pos, y_pos, direction)
    visited_states = set()
    visited_states.add((x_pos, y_pos, direction))

    while True:
        dx, dy = directions[direction]
        next_x, next_y = x_pos + dx, y_pos + dy

        if not (0 <= next_x < max_rows and 0 <= next_y < max_cols):
            # Out of bounds -> stop
            break

        if grid[next_x][next_y] == '#':
            # Turn right and continue
            direction = right_turn[direction]
            continue

        # Move to the next cell
        x_pos, y_pos = next_x, next_y

        # Check if this state has been visited before
        current_state = (x_pos, y_pos, direction)
        if current_state in visited_states:
            return "Infinite loop detected"
        visited_states.add(current_state)

    return visited_states

@timer
def part1(input_lines):
    grid = parse_input(input_lines)
    visited = simulate_movement(grid)
    logging.debug(f"Visited positions: {visited}")
    return len(visited)

@timer
def part2(input_lines):
    grid = parse_input(input_lines)
    max_rows = len(grid)
    max_cols = len(grid[0])
    loop_count = 0
    for x in range(max_rows):
        for y in range(max_cols):
            if grid[x][y] == '.':
                grid[x][y] = '#'
                result = simulate_movement(grid)
                if result == "Infinite loop detected":
                    loop_count += 1
                grid[x][y] = '.'  # Reset the obstacle
    return loop_count

def main():
    sample_mode = '--test' in sys.argv
    input_lines = get_input(day=6, sample=sample_mode)
    configure_logging(debug='--debug' in sys.argv)
    unique_visited_count = part1(input_lines)
    logging.info(f"Unique visited tiles count: {unique_visited_count}")
    loop_count = part2(input_lines)
    logging.info(f"Number of tiles causing infinite loops: {loop_count}")

if __name__ == "__main__":
    main()
