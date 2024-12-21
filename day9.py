def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def parse_input(data: list[str]) -> list[str]:
    return list(map(int, data[0]))


def get_block_data(data: list[str, int]) -> list[str, int]:
    block_data = []
    id_counter = 0

    for i in range(0, len(data), 2):
        for j in range(data[i]):
            block_data.append(id_counter)
        id_counter += 1
        if i+1 == len(data):
            break
        for n in range(data[i+1]):
            block_data.append('.')

    return block_data


def part1(data: list[str]) -> int:
    result = 0
    block_data = []
    switch = True
    id_counter = 0
    for x in data:
        if switch:
            for i in range(x):
                block_data.append(id_counter)
            switch = False
            id_counter += 1
        else:
            for i in range(x):
                block_data.append('.')
            switch = True

    leftcounter = 0
    rightcounter = len(block_data) - 1
    while leftcounter < rightcounter-1:
        if block_data[rightcounter] != '.':
            while block_data[leftcounter] != '.':
                leftcounter += 1
            block_data[leftcounter] = block_data[rightcounter]
            block_data[rightcounter] = '.'

        rightcounter -= 1

    for i, number in enumerate(block_data):
        if number == '.':
            break
        result += i*number

    return result


def part2(data: list[str]) -> int:
    result = 0
    block_data = []
    switch = True
    id_counter = 0
    for x in data:
        if switch:
            for i in range(x):
                block_data.append(id_counter)
            switch = False
            id_counter += 1
        else:
            for i in range(x):
                block_data.append('.')
            switch = True
    # print(data)
    # print(block_data)
    input_map = data.copy()

    right_counter = len(block_data) - 1

    right_counter_map = len(input_map) - 2

    while right_counter_map >= 0:
        found_space = False

        left_counter = 0
        left_counter_map = 0

        while left_counter_map < right_counter_map:
            # go from left to right and find a free spot
            if input_map[left_counter_map+1] >= data[right_counter_map+1]:
                found_space = True
                left_counter += input_map[left_counter_map]
                break
            left_counter += input_map[left_counter_map] + \
                input_map[left_counter_map+1]
            left_counter_map += 2

        if found_space:
            # only after spot is found take behind put it in gap update gap
            tmp = block_data[right_counter]
            input_map[left_counter_map+1] -= input_map[right_counter_map+1]
            input_map[left_counter_map] += input_map[right_counter_map+1]

            for i in range(data[right_counter_map+1]):
                block_data[left_counter] = tmp
                left_counter += 1
                block_data[right_counter] = '.'
                right_counter -= 1

            right_counter -= data[right_counter_map]
        else:
            right_counter -= data[right_counter_map]+data[right_counter_map+1]
        right_counter_map -= 2
        # print(block_data, right_counter_map, input_map[right_counter_map+1])

    # print(input_map)

    for i, number in enumerate(block_data):
        if number != '.':
            result += i*number

    return result


def part22(data: list[str]) -> int:
    result = 0
    block_data = []
    switch = True
    id_counter = 0
    for x in data:
        if switch:
            for i in range(x):
                block_data.append(id_counter)
            switch = False
            id_counter += 1
        else:
            for i in range(x):
                block_data.append('.')
            switch = True

    right_counter = len(block_data) - 1

    current_block_length = 1
    left_counter = 0
    current_gap_length = 0

    while right_counter >= 0:
        # naechster block ist unterschiedlich
        if block_data[right_counter] != block_data[right_counter-1]:
            # counter link und gap 0
            left_counter = 0
            current_gap_length = 0
            # wenn derzeitiger block ein punkt ist dann weiter
            if block_data[right_counter] == '.':
                right_counter -= 1
                # current_block_length = 0
                continue
            # gap finden
            while left_counter < right_counter:
                if block_data[left_counter] == '.':
                    current_gap_length += 1
                else:
                    current_gap_length = 0
                if current_gap_length >= current_block_length:
                    # gap gefunden
                    tmp = block_data[right_counter]
                    for i in range(current_block_length):
                        block_data[left_counter-i] = tmp
                        block_data[right_counter + i] = '.'
                    break
                left_counter += 1
            print(block_data,right_counter,current_block_length)
            current_block_length = 0

        current_block_length += 1
        right_counter -= 1

    for i, number in enumerate(block_data):
        if number != '.':
            result += i*number

    return result


if __name__ == "__main__":
    input_data = read_input('input/input9.txt')
    test_input_data = read_input('input/testinput9.txt')
    input_data = parse_input(input_data)
    test_input_data = parse_input(test_input_data)
    print(get_block_data(test_input_data))
    # print("Part 1:", part1(input_data))
    # print("Part 2:", part22(test_input_data))
