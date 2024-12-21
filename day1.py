from collections import Counter


def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def parse_input(data):
    column1 = []
    column2 = []
    for line in data:
        x = line.split()
        column1.append(int(x[0]))
        column2.append(int(x[1]))
    return column1, column2


def part1(data):
    column1, column2 = parse_input(data)
    column1.sort()
    column2.sort()
    return sum(abs(c1 - c2) for c1, c2 in zip(column1, column2))


def part2(data):
    column1, column2 = parse_input(data)
    column1.sort()
    column2.sort()

    c2_counts = Counter(column2)
    return sum(c1 * c2_counts[c1] for c1 in set(column1) if c1 in c2_counts)


if __name__ == "__main__":
    input_data = read_input('input/input1.txt')
    test_data = read_input('input/testinput1.txt')
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))
