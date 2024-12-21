def read_input(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


def part1(data):
    data = list(map(lambda x: list(x.strip()), data))
    state = 0
    column = 0
    row = 0
    end = False
    count = 0

    # find the starting position of the guard
    for r, line in enumerate(data):
        for col, char in enumerate(line):
            if char == '^':
                column = col
                row = r
                state = 1
                break

# ^ > v <
    while not end:
        if state == 1:
            while row - 1 >= 0:
                data[row][column] = 'X'
                if data[row - 1][column] == '#':
                    state = 2
                    break
                row -= 1
            if row == 0:
                end = True

        if state == 2:
            while column + 1 < len(data[0]):
                data[row][column] = 'X'
                if data[row][column + 1] == '#':
                    state = 3
                    break
                column += 1
            if column == len(data[0]):
                end = True

        if state == 3:
            while row + 1 < len(data):
                data[row][column] = 'X'
                if data[row+1][column] == '#':
                    state = 4
                    break
                row += 1
            if row == len(data)-1:
                end = True

        if state == 4:
            while column - 1 >= 0:
                data[row][column] = 'X'
                if data[row][column - 1] == '#':
                    state = 1
                    break
                column -= 1
            if column == 0:
                end = True
        
        if end:
            break
    
    for d in data:
        for c in d:
            if c == 'X':
                count += 1
        print(d)
    
    count += 1 # because it bound of last step
    return count


def part2(data):
    data = list(map(lambda x: list(x.strip()), data))
    state = 0
    column = 0
    row = 0
    end = False
    count = 0

    # find the starting position of the guard
    for r, line in enumerate(data):
        for col, char in enumerate(line):
            if char == '^':
                column = col
                row = r
                state = 1
                break

# ^ > v <
    while not end:
        if state == 1:
            while row - 1 >= 0:
                data[row][column] = 'X'
                if data[row - 1][column] == '#':
                    state = 2
                    break
                row -= 1
            if row == 0:
                end = True

        if state == 2:
            while column + 1 < len(data[0]):
                data[row][column] = 'X'
                if data[row][column + 1] == '#':
                    state = 3
                    break
                column += 1
            if column == len(data[0]):
                end = True

        if state == 3:
            while row + 1 < len(data):
                data[row][column] = 'X'
                if data[row+1][column] == '#':
                    state = 4
                    break
                row += 1
            if row == len(data)-1:
                end = True

        if state == 4:
            while column - 1 >= 0:
                data[row][column] = 'X'
                if data[row][column - 1] == '#':
                    state = 1
                    break
                column -= 1
            if column == 0:
                end = True
        
        if end:
            break
    
    for d in data:
        for c in d:
            if c == 'X':
                count += 1
        print(d)
    
    count += 1 # because it bound of last step
    return count


if __name__ == "__main__":
    input_data = read_input('input/input6.txt')
    # print("Part 1:", part1(input_data))
    print("Part 2:", part2(input_data))
