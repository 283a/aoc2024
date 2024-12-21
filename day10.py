from typing import Set, Tuple
import numpy as np


def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def parse_input(data: list[str]) -> np.ndarray:
    return np.array([list(map(int, row)) for row in data])


def part1(data: np.ndarray) -> int:

    row_length, column_length = data.shape

    def reku(i: int, j: int, visited: Set[Tuple[int, int]]) -> int:

        if (i, j) in visited:
            return 0
        visited.add((i, j))
        value = data[i][j]

        if value == 9:
            return 1

        next_value = value + 1

        total = 0

        if i > 0 and data[i-1][j] == next_value:
            total += reku(i-1, j, visited)
        if i < row_length - 1 and data[i+1][j] == next_value:
            total += reku(i+1, j, visited)
        if j > 0 and data[i][j-1] == next_value:
            total += reku(i, j-1, visited)
        if j < column_length - 1 and data[i][j+1] == next_value:
            total += reku(i, j+1, visited)

        return total

    result = 0
    for i in range(row_length):
        for j in range(column_length):
            if data[i][j] == 0:
                paths = reku(i, j, set())
                result += paths

    return result


def part2(data: np.ndarray) -> int:

    row_length, column_length = data.shape

    def reku(i: int, j: int) -> int:

        value = data[i][j]

        if value == 9:
            return 1

        next_value = value + 1

        total = 0

        if i > 0 and data[i-1][j] == next_value:
            total += reku(i-1, j)
        if i < row_length - 1 and data[i+1][j] == next_value:
            total += reku(i+1, j)
        if j > 0 and data[i][j-1] == next_value:
            total += reku(i, j-1)
        if j < column_length - 1 and data[i][j+1] == next_value:
            total += reku(i, j+1)

        return total

    result = 0
    for i in range(row_length):
        for j in range(column_length):
            if data[i][j] == 0:
                paths = reku(i, j)
                result += paths

    return result


if __name__ == "__main__":
    input_data = read_input('input/input10.txt')
    test_input_data = read_input('input/testinput10.txt')
    input_data = parse_input(input_data)
    test_input_data = parse_input(test_input_data)
    print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))
