def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def parse_input(data):
    return [
        [int(x[:-1]) if i == 0 else int(x) for i, x in enumerate(line.split())]
        for line in data
    ]


def calculate(last_value: int, rest_list: list[int], result: int):
    if len(rest_list) == 1:
        if last_value + rest_list[0] == result \
                or last_value * rest_list[0] == result:
            return True
        return False

    return calculate(last_value + rest_list[0], rest_list[1:], result) or \
        calculate(last_value * rest_list[0], rest_list[1:], result)


def calculate2(last_value: int, rest_list: list[int], result: int):
    if len(rest_list) == 1:
        if last_value + rest_list[0] == result \
                or last_value * rest_list[0] == result \
                or int(str(last_value) + str(rest_list[0])) == result:
            return True
        return False

    return calculate2(last_value + rest_list[0], rest_list[1:], result) or \
        calculate2(last_value * rest_list[0], rest_list[1:], result) or \
        calculate2(int(str(last_value) + str(rest_list[0])), rest_list[1:], result)


def part1(data):
    result = 0
    for line in data:
        if calculate(line[1], line[2:], line[0]):
            result += line[0]

    return result


def part2(data):
    result = 0
    for line in data:
        if calculate2(line[1], line[2:], line[0]):
            result += line[0]

    return result


if __name__ == "__main__":
    input_data = read_input('input/input7.txt')
    test_input_data = read_input('input/testinput7.txt')
    input_data = parse_input(input_data)
    test_input_data = parse_input(test_input_data)
    # print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))
