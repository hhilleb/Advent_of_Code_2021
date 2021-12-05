import re

with open('inputs/aoc_2021_input_2.txt') as f:
    commands = [line.rstrip().split(" ") for line in f]

def part1(commands):
    horizontal = sum([int(c[1]) for c in commands if c[0] == 'forward'])
    depth = sum([int(c[1]) if c[0] == 'down' else -int(c[1]) if c[0] == 'up' else 0 for c in commands])
    return horizontal * depth

def part2(commands):
    horizontal, depth, aim = 0, 0, 0
    for c in commands:
        if c[0] == 'down':
            aim += int(c[1])
        elif c[0] == 'up':
            aim -= int(c[1])
        else:
            horizontal += int(c[1])
            depth += int(c[1]) * aim
    return horizontal * depth


print("Part 1: " + str(part1(commands)))
print("Part 1: " + str(part2(commands)))