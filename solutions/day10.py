import sys
import os
import logging
from collections import deque

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.aoc_utils import get_input, timer, configure_logging

@timer
def part1(input_lines):
    height_map = []
    for line in input_lines:
        row = [int(char) for char in line.strip()]
        height_map.append(row)

    rows = len(height_map)
    cols = len(height_map[0])
    
    # Directions for up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Find all trail heads (cells with height 0)
    trail_heads = []
    for i in range(rows):
        for j in range(cols):
            if height_map[i][j] == 0:
                trail_heads.append((i, j))

    # Find all trail ends (cells with max height)
    max_height = max(max(row) for row in height_map)
    trail_ends = []
    for i in range(rows):
        for j in range(cols):
            if height_map[i][j] == max_height:
                trail_ends.append((i, j))

    def bfs(start):
        queue = deque([start])
        visited = set()
        visited.add(start)
        reachable_ends = 0
        
        while queue:
            x, y = queue.popleft()
            
            if (x, y) in trail_ends:
                reachable_ends += 1
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    if height_map[nx][ny] == height_map[x][y] + 1:
                        queue.append((nx, ny))
                        visited.add((nx, ny))
        
        return reachable_ends

    # Count how many trail ends can be reached from each trail head
    total_reachable_ends = 0
    for head in trail_heads:
        total_reachable_ends += bfs(head)
    
    return total_reachable_ends

@timer
def part2(input_lines):
    height_map = []
    for line in input_lines:
        row = [int(char) for char in line.strip()]
        height_map.append(row)

    rows = len(height_map)
    cols = len(height_map[0])
    
    # Directions for up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Find all trail heads (cells with height 0)
    trail_heads = []
    for i in range(rows):
        for j in range(cols):
            if height_map[i][j] == 0:
                trail_heads.append((i, j))

    def dfs(x, y, visited):
        if height_map[x][y] == 9:
            return 1
        visited.add((x, y))
        total_trails = 0
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if height_map[nx][ny] == height_map[x][y] + 1:
                    total_trails += dfs(nx, ny, visited)
        visited.remove((x, y))
        return total_trails

    total_trails = 0
    for head in trail_heads:
        total_trails += dfs(head[0], head[1], set())

    return total_trails

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
