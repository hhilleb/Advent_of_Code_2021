import copy

with open('inputs/aoc_2021_input_3.txt') as f:
    numbers = [line.rstrip() for line in f]

def get_criteria_bit(numbers, pos, criteria):
    zero_count = 0
    one_count = 0
    for number in numbers:
        if number[pos] == '0':
            zero_count += 1
        else:
            one_count += 1
    if criteria == 'oxygen':
        return '0' if zero_count > one_count else '1'
    elif criteria == 'co2':
        return '1' if zero_count > one_count else '0'

def part1(numbers):
    gamma = ""
    for pos in range(len(numbers[0])):
        gamma += get_criteria_bit(numbers, pos, 'oxygen')
    epsilon = ''.join('1' if x == '0' else '0' for x in gamma)
    return int(gamma, 2) * int(epsilon, 2)

def part2(numbers):
    oxygen_numbers = copy.deepcopy(numbers)
    co2_numbers = copy.deepcopy(numbers)
    for pos in range(len(numbers[0])):
        if len(oxygen_numbers) > 1:
            oxygen_mcb = get_criteria_bit(oxygen_numbers, pos, 'oxygen')
            oxygen_numbers = [num for num in oxygen_numbers if num[pos] == oxygen_mcb]
        if len(co2_numbers) > 1:
            co2_mcb = get_criteria_bit(co2_numbers, pos, 'co2')
            co2_numbers = [num for num in co2_numbers if num[pos] == co2_mcb]
    return int(oxygen_numbers[0], 2) * int(co2_numbers[0], 2)
           

print("Part 1: " + str(part1(numbers)))
print("Part 2: " + str(part2(numbers)))