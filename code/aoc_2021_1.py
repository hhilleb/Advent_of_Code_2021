with open('inputs/aoc_2021_input_1.txt') as f:
    depths = [int(line.rstrip()) for line in f]

def part1(depths):
    increase_count = 0
    for i in range(len(depths)-1):
        if depths[i] < depths[i+1]:
            increase_count += 1
    return increase_count

def part2(dephts):
    window_increase_count = 0
    for i in range(len(dephts)-3):
        if sum(dephts[i:i+3]) < sum(dephts[i+1:i+4]):
            window_increase_count += 1
    return window_increase_count

print("Part 1: " + str(part1(depths)))
print("Part 2: " + str(part2(depths)))