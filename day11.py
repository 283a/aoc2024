from typing import Set, Tuple
import numpy as np


def read_input(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def parse_input(data: list[str]) -> np.ndarray:
    return [int(x) for x in data[0].split(' ')]


def part1(data: list[int]) -> int:

    def get_number_length(num: int) -> int:
        result = 0
        while num > 0:
            num //= 10
            result += 1
        return result

    for n in range(25):
        current_length = len(data)
        i = 0
        while i < current_length:
            value = data[i]
            num_digits = get_number_length(value)
            if value == 0:
                data[i] = 1
            elif num_digits % 2 == 0:
                split_factor = 10 ** (num_digits // 2)
                data.pop(i)
                data.insert(i, value // split_factor)
                data.insert(i+1, value % split_factor)
                i += 1
                current_length += 1
            else:
                data[i] *= 2024
            i += 1
    return len(data)


def part2(data: list[int]) -> int:

    def get_number_length(num: int) -> int:
        result = 0
        while num > 0:
            num //= 10
            result += 1
        return result

    values = {}
    
    for x in data:
        values[x] = 1
    
    for _ in range(75):
        new_values = {}
        for number, count in values.items():
            if number == 0:
                if 1 in new_values:
                    new_values[1] += count
                else:
                    new_values[1] = count
            else:
                num_digits = get_number_length(number)
                if num_digits % 2 == 0:
                    split_factor = 10 ** (num_digits // 2)
                    if number // split_factor in new_values:
                        new_values[number // split_factor] += count
                    else:
                        new_values[number // split_factor] = count
                    if number % split_factor in new_values:
                        new_values[number % split_factor] += count
                    else:
                        new_values[number % split_factor] = count
                else:
                    if number * 2024 in new_values:
                        new_values[number * 2024] += count
                    else:
                        new_values[number * 2024] = count
        values = new_values
    result = 0
    for number, count in values.items():
        result += count

    return result


if __name__ == "__main__":
    input_data = read_input('input/input11.txt')
    test_input_data = read_input('input/testinput11.txt')
    input_data = parse_input(input_data)
    test_input_data = parse_input(test_input_data)
    # print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))
