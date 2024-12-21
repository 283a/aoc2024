def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]


def parse_input(data: list[str]) -> tuple[list[tuple[str, str]], list[str]]:
    rules = []
    updates = []

    switch_index = data.index('')

    for row in data[:switch_index]:
        left, right = map(int, row.split('|'))
        rules.append((left, right))

    for row in data[switch_index + 1:]:
        update = [int(num) for num in row.split(',')]
        updates.append(update)

    return rules, updates


def part1(data: tuple) -> int:
    rules, updates = data
    result = 0

    for update in updates:
        legit = True
        for i, _ in enumerate(update):
            if i == 0:
                continue
            legit = legit and ((update[i-1], update[i]) in rules)
        if legit:
            print(update)
            result += update[len(update)//2]

    return result


def part2(data: tuple):
    rules, updates = data
    result = 0
    incorrect_updates = []

    for update in updates:
        legit = True
        for i, _ in enumerate(update):
            if i == 0:
                continue
            legit = legit and ((update[i-1], update[i]) in rules)
        if not legit:
            incorrect_updates.append(update)

    for update in incorrect_updates:

        for i in range(1, len(update)):
            is_rule = (update[i-1], update[i]) in rules

            if not is_rule:
                tmp = update[i]
                update[i] = update[i-1]
                update[i-1] = tmp
                for j in reversed(range(1, i)):
                    is_rule = (update[j-1], update[j]) in rules
                    if not is_rule:
                        tmp = update[j]
                        update[j] = update[j-1]
                        update[j-1] = tmp
        result += update[len(update)//2]

    return result


if __name__ == "__main__":
    input_data = read_input('input/input5.txt')
    test_input_data = read_input('input/testinput5.txt')
    input_data = parse_input(input_data)
    test_input_data = parse_input(test_input_data)
    # print("Part 1:", part1(test_input_data))
    print("Part 2:", part2(input_data))
