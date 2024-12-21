import re


def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.read()


def solve_part1(data):
    pattern = re.compile(r'mul\(\d+,\d+\)')
    result = 0
    match = re.findall(pattern, data)
    for m in match:
        extracted = m.split('(')[1].split(')')[0].split(',')
        result += int(extracted[0]) * int(extracted[1])

    return result


def solve_part2(data):
    pattern = re.compile(r"mul\(\d+,\d+\)|do\(\)|don\'t\(\)")
    result = 0
    match = re.findall(pattern, data)
    do = True
    for m in match:
        if m == "do()":
            do = True
        elif m == "don't()":
            do = False
        elif do:
            extracted = m.split('(')[1].split(')')[0].split(',')
            result += int(extracted[0]) * int(extracted[1])

    return result


if __name__ == "__main__":
    input_data = read_input('input3.txt')
    print("Part 1:", solve_part1(input_data))
    print("Part 2:", solve_part2(input_data))
