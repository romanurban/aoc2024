import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.aoc_utils import get_input, timer

@timer
def part1(input_lines):
    left = []
    right = []
    for line in input_lines:
        values = line.split()
        if len(values) >= 2:
            left.append(int(values[0]))
            right.append(int(values[1]))

    left.sort()
    right.sort()

    differences = []
    for l, r in zip(left, right):
        difference = abs(l - r)
        differences.append(difference)

    total_difference = sum(differences)

    return total_difference

@timer
def part2(input_lines):
    left = []
    right = []
    for line in input_lines:
        values = line.split()
        if len(values) >= 2:
            left.append(int(values[0]))
            right.append(int(values[1]))

    left.sort()
    right.sort()

    similarity_score = []
    for l in left:
        frequency = right.count(l)
        score = frequency * l
        similarity_score.append(score)

    #print("left list:", left)
    #print("right list:", right)
    #print("similarity score:", similarity_score)

    total_score = sum(similarity_score)
    return total_score

def main():
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

if __name__ == "__main__":
    main()
