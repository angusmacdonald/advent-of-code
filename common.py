from typing import List


def parse_grid_from_file(file: str) -> List[List[str]]:
    with open(file) as f:
        return [[c for c in line.strip()] for line in f.readlines()]


def print_grid(grid: List[List[str]]):
    for line in grid:
        print(''.join(line))
    print('')
