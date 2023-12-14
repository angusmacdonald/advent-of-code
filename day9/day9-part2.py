from typing import List
import pprint
import logging


def load_lines_from_file() -> List[str]:
    with open('day9/input.txt') as f:
        return f.readlines()


def get_array_of_arrays(lines: List[str]) -> List[List[int]]:
    return [[int(x) for x in line.lstrip().strip().split(' ')] for line in lines]


lines = get_array_of_arrays(load_lines_from_file())


def calc(line: List[int]) -> int:
    stack: List[List[int]] = []
    stack.append(line)

    while not all(entry == 0 for entry in line):
        copy = []
        for i in range(1, len(line)):
            copy.append(line[i] - line[i-1])
        line = copy
        stack.append(copy)

    pprint.pprint(stack)

    last = 0
    logging.debug(f'stack: {stack}')
    while len(stack) > 0:
        line = stack.pop()
        logging.debug(f'line: {line}')
        next_last = line[0]
        logging.debug(f'next_last: {next_last}')

        last = next_last-last
        logging.debug(f'last: {last}')
    return last


total = 0
for line in lines:
    print(line)
    total += calc(line)
    print(f'result: {total}')

print(f'total: {total}')
