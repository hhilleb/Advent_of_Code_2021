from collections import defaultdict

with open('inputs/aoc_2021_input_5.txt') as f:
    vents = []
    for line in f:
        point1, point2 = line.rstrip().split(" -> ")
        vents.append([[int(x) for x in point1.split(",")], [int(x) for x in point2.split(",")]])

def part1(vents):
    vent_coords = defaultdict(lambda : 0)
    for vent in vents:
        x1 = vent[0][0]
        y1 = vent[0][1]
        x2 = vent[1][0]
        y2 = vent[1][1]
        if x1 == x2:
            for i in range(abs(y1 - y2) + 1):
                vent_coords[x1, min(y1, y2) + i] += 1
        elif y1 == y2:
            for i in range(abs(x1 - x2) + 1):
                vent_coords[min(x1, x2) + i, y1] += 1
    return len([count for count in vent_coords.values() if count > 1])

def part2(vents):
    vent_coords = defaultdict(lambda : 0)
    for vent in vents:
        x1 = vent[0][0]
        y1 = vent[0][1]
        x2 = vent[1][0]
        y2 = vent[1][1]
        if x1 == x2:
            for i in range(abs(y1 - y2) + 1):
                vent_coords[x1, min(y1, y2) + i] += 1
        elif y1 == y2:
            for i in range(abs(x1 - x2) + 1):
                vent_coords[min(x1, x2) + i, y1] += 1
        elif x1 < x2 and y1 < y2:
            for i in range(abs(x1 - x2) + 1):
                vent_coords[x1 + i, y1 + i] += 1
        elif x1 < x2 and y1 > y2:
            for i in range(abs(x1 - x2) + 1):
                vent_coords[x1 + i, y1 - i] += 1
        elif x1 > x2 and y1 < y2:
            for i in range(abs(x1 - x2) + 1):
                vent_coords[x1 - i, y1 + i] += 1
        else:
            for i in range(abs(x1 - x2) + 1):
                vent_coords[x1 - i, y1 - i] += 1
    return len([count for count in vent_coords.values() if count > 1])

      
print("Part 1: " + str(part1(vents)))
print("Part 2: " + str(part2(vents)))