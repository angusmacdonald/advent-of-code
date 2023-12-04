from typing import List
import logging
from itertools import groupby


def load_matrix_from_file() -> List[List[str]]:
    with open('day3/input.txt') as f:
        return [list(line.strip()) for line in f.readlines()]


def find_numbers(matrix: List[List[str]]) -> List[dict]:
    results = []
    for y in range(0, len(matrix)):
        row = matrix[y]

        num_str = ''
        start_idx = None

        for x in range(0, len(row)):
            char = row[x]
            if char.isnumeric():
                if num_str == '':
                    start_idx = x
                num_str += char
                if len(row)-1 == x or not row[x+1].isnumeric():
                    results.append({'row': y, 'start': start_idx,
                                   'end': x, 'number': int(num_str)})
                    num_str = ''
                    start_idx = None

    return results


def is_sym(symbol: str) -> bool:
    return symbol != '.' and not symbol.isnumeric()


def is_valid_number(y, x_min, x_max, matrix: List[List[str]], is_match_fn) -> str:
    if y > 0:
        for x in range(max(0, x_min-1), min(x_max+2, len(matrix[y-1]))):
            if is_match_fn(matrix[y-1][x]):
                logging.debug(f'Found {matrix[y-1][x]}')
                return str(y-1) + ',' + str(x)
    if y < len(matrix)-1:
        for x in range(max(0, x_min-1), min(x_max+2, len(matrix[y+1]))):
            if is_match_fn(matrix[y+1][x]):
                logging.debug(f'Found {matrix[y+1][x]}')
                return str(y+1) + ',' + str(x)
    if x_min > 0 and is_match_fn(matrix[y][x_min-1]):
        logging.debug(f'Found {matrix[y][x_min-1]}')
        return str(y) + ',' + str(x_min-1)
    if x_max < len(matrix[y])-1 and is_match_fn(matrix[y][x_max+1]):
        logging.debug(f'Found {matrix[y][x_max+1]}')
        return str(y) + ',' + str(x_max+1)

    return None


matrix = load_matrix_from_file()

numbers = find_numbers(matrix)
filtered_numbers = list(
    filter(lambda number: is_valid_number(number['row'], number['start'], number['end'], matrix, is_sym) is not None,
           numbers)
)
only_numbers = list(map(lambda number: number['number'], filtered_numbers))
print(only_numbers)
print(sum(only_numbers))


number_with_key = list(
    map(lambda number: {'cog': is_valid_number(number['row'], number['start'], number['end'], matrix, (lambda x: x == "*")), 'number': number['number']},
        filtered_numbers)
)

print(number_with_key)

# sort by 'cog' field

no_none = list(
    filter(lambda entry: entry['cog'] is not None,
           number_with_key))

no_none.sort(key=lambda x: x['cog'])
sum = 0
for cog, entries in groupby(no_none, lambda x: x['cog']):
    entry_list = list(entries)
    if len(entry_list) == 2:
        print(f'number: {cog}, entries: {entry_list}')
        sum += (entry_list[0]['number'] * entry_list[1]['number'])
    else:
        print(f'number: {cog}, entries: {entry_list}')

print(sum)

# reduce to those with same cog
# 467835
