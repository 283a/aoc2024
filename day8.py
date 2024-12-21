def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def parse_input(data):
    return [list(line) for line in data]


def find_antennas(data):
    antennas = {}
    for y, row in enumerate(data):
        for x, column in enumerate(row):
            if column[0] != '.':
                if column[0] not in antennas:
                    antennas[column[0]] = [(y, x)]
                else:
                    antennas[column[0]].append((y, x))
    return antennas


def count_antinodes(data):
    counter = 0
    for row in data:
        for column in row:
            if len(column) > 1 and column[1] == '#':
                counter += 1

    return counter


def part1(data):

    antennas = find_antennas(data)

    for _, points in antennas.items():
        for y, x in points:
            for y2, x2 in points:
                if y == y2 and x == x2:
                    continue
                x3 = x + ((x2 - x) * 2)
                y3 = y + ((y2 - y) * 2)

                if 0 <= x3 < len(data) and 0 <= y3 < len(data[0]):
                    data[y3][x3] += "#"

    return count_antinodes(data)


def part2(data):

    antennas = find_antennas(data)

    for _, points in antennas.items():
        for y, x in points:
            for y2, x2 in points:
                if y == y2 and x == x2:
                    if len(data[y][x]) == 1:
                        data[y][x] += "#"
                    continue
                multiple = 2
                x3 = x + ((x2 - x) * multiple)
                y3 = y + ((y2 - y) * multiple)

                if 0 <= x3 < len(data) and 0 <= y3 < len(data[0]):
                    data[y3][x3] += "#"

                while 0 <= x3 < len(data) and 0 <= y3 < len(data[0]):
                    x3 = x + ((x2 - x) * multiple)
                    y3 = y + ((y2 - y) * multiple)
                    multiple = multiple + 1

                    if 0 <= x3 < len(data) and 0 <= y3 < len(data[0]):
                        if len(data[y3][x3]) == 1:
                            data[y3][x3] += "#"

    return count_antinodes(data)


if __name__ == "__main__":
    input_data = read_input('input/input8.txt')
    input_data = parse_input(input_data)
    # print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))
