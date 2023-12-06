import logging
from typing import List


def load_lines_from_file() -> List[str]:
    with open('day6/input.txt') as f:
        return f.readlines()


def parse_nums_from_line(line: str, ignore_prefix: str) -> dict:
    # Time:      7  15   30
    # Distance:  9  40  200

    line = line.removeprefix(ignore_prefix).strip().lstrip()

    numbers = []
    builder = ''

    for char in line:
        if char.isnumeric():
            builder += char
        elif builder != '':
            numbers.append(int(builder))
            builder = ''
    if builder != '':
        numbers.append(int(builder))

    logging.debug(numbers)

    return numbers


def parse_with_no_spaces(line: str, ignore_prefix: str) -> int:
    # Time:      7  15   30
    # Distance:  9  40  200

    line = line.removeprefix(ignore_prefix).strip().lstrip()
    return int(line.replace(' ', ''))


def calculate_record_beaters(time: int, distance: int):
    winners = []

    for i in range(0, time):
        speed_per_sec = i
        record_to_beat = distance
        time_left = time - i

        new_time = time_left * speed_per_sec

        logging.debug(
            f'{i} speed: {speed_per_sec} record: {record_to_beat} time left: {time_left} new time: {new_time}')

        if new_time > record_to_beat:
            winners.append(speed_per_sec)

    return winners


def part1() -> int:
    lines = load_lines_from_file()
    time = parse_nums_from_line(lines[0], 'Time:')
    distance = parse_nums_from_line(lines[1], 'Distance:')

    count = 1

    for i in range(0, len(time)):
        winners = calculate_record_beaters(time[i], distance[i])
        count *= len(winners)

    return count


def part2() -> int:
    lines = load_lines_from_file()

    time = parse_with_no_spaces(lines[0], 'Time:')
    distance = parse_with_no_spaces(lines[1], 'Distance:')

    winners = calculate_record_beaters(time, distance)
    return len(winners)


print(part1())
print(part2())
