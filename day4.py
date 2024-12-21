def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def parse_input(data: list[str]) -> list[list[str]]:
    return [list(row) for row in data]


def part1(data):
    result = 0

    for i, row in enumerate(data):
        for j in range(0, len(row)):
            if row[j] == 'X':
                # row check 
                if j-3 >= 0 and row[j-1] == 'M' and row[j-2] == 'A' and row[j-3] == 'S':
                    result += 1
                if j+3 < len(row) and row[j+1] == 'M' and row[j+2] == 'A' and row[j+3] == 'S':
                    result += 1
                # column check
                if i-3 >= 0 and data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-3][j] == 'S':
                    result += 1
                if i+3 < len(data) and data[i+1][j] == 'M' and data[i+2][j] == 'A' and data[i+3][j] == 'S':
                    result += 1
                # diagonal check
                if j-3 >= 0 and i-3 >= 0 and data[i-1][j-1] == 'M' and data[i-2][j-2] == 'A' and data[i-3][j-3] == 'S':
                    result += 1
                if j+3 < len(row) and i-3 >= 0 and data[i-1][j+1] == 'M' and data[i-2][j+2] == 'A' and data[i-3][j+3] == 'S':
                    result += 1
                if j-3 >= 0 and i+3 < len(data) and data[i+1][j-1] == 'M' and data[i+2][j-2] == 'A' and data[i+3][j-3] == 'S':
                    result += 1
                if j+3 < len(row) and i+3 < len(data) and data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S':
                    result += 1

    return result


def part2(data):
    result = 0

    for i, row in enumerate(data):
        for j in range(0, len(row)):
            if row[j] == 'A':
                if (j-1 >= 0 and i-1>= 0 and data[i-1][j-1] == 'M') \
                    and (j+1 < len(row) and i-1>= 0 and data[i-1][j+1] == 'S')\
                    and (j-1 >= 0 and i+1 < len(data) and data[i+1][j-1] == 'M')\
                    and (j+1 < len(row) and i+1 < len(data) and data[i+1][j+1] == 'S'):
                    result += 1
                elif (j-1 >= 0 and i-1>= 0 and data[i-1][j-1] == 'M') \
                    and (j+1 < len(row) and i-1>= 0 and data[i-1][j+1] == 'M')\
                    and (j-1 >= 0 and i+1 < len(data) and data[i+1][j-1] == 'S')\
                    and (j+1 < len(row) and i+1 < len(data) and data[i+1][j+1] == 'S'):
                    result += 1
                elif (j-1 >= 0 and i-1>= 0 and data[i-1][j-1] == 'S') \
                    and (j+1 < len(row) and i-1>= 0 and data[i-1][j+1] == 'S')\
                    and (j-1 >= 0 and i+1 < len(data) and data[i+1][j-1] == 'M')\
                    and (j+1 < len(row) and i+1 < len(data) and data[i+1][j+1] == 'M'):
                    result += 1
                elif (j-1 >= 0 and i-1>= 0 and data[i-1][j-1] == 'S') \
                    and (j+1 < len(row) and i-1>= 0 and data[i-1][j+1] == 'M')\
                    and (j-1 >= 0 and i+1 < len(data) and data[i+1][j-1] == 'S')\
                    and (j+1 < len(row) and i+1 < len(data) and data[i+1][j+1] == 'M'):
                    result += 1

    return result


if __name__ == "__main__":
    input_data = read_input('input/input4.txt')
    test_input_data = read_input('input/testinput4.txt')
    input_data = parse_input(input_data)
    test_input_data = parse_input(test_input_data)
    # print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))
