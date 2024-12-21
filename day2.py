def part1():
    reports = []

    with open('input2.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            numbers = line.split()
            numbers = [int(number) for number in numbers]
            reports.append(numbers)

    safe_count = 0
    for report in reports:
        if report[0] < report[1]:
            increasing = True
        else:
            increasing = False

        previous_number = report[0]
        safe = True

        for i in range(1, len(report)):
            if abs(report[i] - previous_number) > 3:
                safe = False
                break
            if previous_number >= report[i] and increasing:
                safe = False
                break
            if previous_number <= report[i] and not increasing:
                safe = False
                break
            previous_number = report[i]

        if safe:
            safe_count += 1
        # print(f"{safe} report: {report}")

    print(safe_count)


def part2():
    # TODO change loop in loop to one loop
    reports = []

    with open('input2.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            numbers = line.split()
            numbers = [int(number) for number in numbers]
            reports.append(numbers)

    safe_count = 0
    safe_count2 = 0
    for report in reports:

        skip = True
        increasing = True
        previous_number = report[0]
        safe = True

        for i in range(1, len(report)):
            if i == 1:
                if report[0] > report[1]:
                    increasing = False
            if abs(report[i] - previous_number) > 3:
                if skip:
                    skip = False
                    continue
                safe = False
                break
            if previous_number >= report[i] and increasing:
                if skip:
                    skip = False
                    continue
                safe = False
                break
            if previous_number <= report[i] and not increasing:
                if skip:
                    skip = False
                    continue
                safe = False
                break
            previous_number = report[i]

        if safe:
            safe_count += 1
        # print(f"{safe} report: {report}")

        if not safe:
            increasing = True
            previous_number = report[1]
            safe = True

            for i in range(2, len(report)):
                if i == 2:
                    if report[1] > report[2]:
                        increasing = False
                if abs(report[i] - previous_number) > 3:
                    safe = False
                    break
                if previous_number >= report[i] and increasing:
                    if skip:
                        skip = False
                        continue
                    safe = False
                    break
                if previous_number <= report[i] and not increasing:
                    if skip:
                        skip = False
                        continue
                    safe = False
                    break
                previous_number = report[i]

            if safe:
                safe_count2 += 1
                print(f"{safe} report: {report}")

    print(safe_count, safe_count2)


part2()
