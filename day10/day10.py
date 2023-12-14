from typing import List, Dict
import pprint
import logging


def parse_grid_from_file() -> List[List[str]]:
    with open('day10/test.txt') as f:
        return [[c for c in line.strip()] for line in f.readlines()]


def find_start(grid: List[List[str]]) -> Dict[int, int]:
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                return [x, y]


def get_valid_directions(char: str) -> Dict[int, int]:
    #     | is a vertical pipe connecting north and south.
    # - is a horizontal pipe connecting east and west.
    # L is a 90-degree bend connecting north and east.
    # J is a 90-degree bend connecting north and west.
    # 7 is a 90-degree bend connecting south and west.
    # F is a 90-degree bend connecting south and east.
    # . is ground; there is no pipe in this tile.
    # S is the starting position of the animal;

    logging.debug(f'get_dir_for: {char}')
    north = [-1, 0]
    west = [0, -1]
    east = [0, 1]
    south = [1, 0]

    if char == '|':
        return [north, south]
    elif char == '-':
        return [west, east]
    elif char == 'L':
        return [north, east]
    elif char == 'J':
        return [north, west]
    elif char == '7':
        return [south, west]
    elif char == 'F':
        return [south, east]
    elif char == 'S':
        return [east, south, west, north]
    else:
        return []


def get_next(grid: List[List[str]], current: Dict[int, int],
             previous: Dict[int, int]) -> Dict[int, int]:
    surrounding = []
    y = current[0]
    x = current[1]

    surrounding = get_valid_directions(grid[y][x])
    logging.debug(f'surrounding: {surrounding}')
    for y_offset, x_offset in surrounding:
        val = grid[y+y_offset][x+x_offset]

        possible_next = [y+y_offset, x+x_offset]
        grid_char = grid[y+y_offset][x+x_offset]
        next_valid_dir = get_valid_directions(grid_char)
        logging.debug(
            f'possible_next: {possible_next} previous: {previous} next_valid_dir: {next_valid_dir}, grid_char: {grid_char}')
        if (y+y_offset is not previous[0] or x+x_offset is not previous[1]) and get_valid_directions(grid_char):
            return possible_next, current

    return None, None


def print_grid(grid: List[List[str]]):
    for line in grid:
        print(''.join(line))
    print('')


def fill_grid(grid: List[List[str]], pos: Dict[int, int]):
    print_grid(grid)
    if grid[pos[0]][pos[1]] == 'X':
        return
    for x in range(-1, 1):
        for y in range(-1, 1):
            if x == 0 and y == 0:
                continue
            grid[pos[0]+y][pos[1]+x] = '#'
            fill_grid(grid, [y, x])


grid = parse_grid_from_file()

start_x, start_y = find_start(grid)

visited: List[Dict[int, int]] = []

last_char = None
pos = [start_y, start_x]
previous = [-1, -1]

grid_visual = parse_grid_from_file()

while last_char != 'S':
    pos, previous = get_next(grid, pos, previous)
    visited.append(pos)
    last_char = grid[pos[0]][pos[1]]

    logging.debug(f'pos: {pos}')
    logging.debug(f'last_char: {last_char}')
    grid_visual[pos[0]][pos[1]] = 'X'


logging.debug(visited)
print(f'visited: {len(visited)}')
print(int(len(visited)/2))

print_grid(grid_visual)
# print(fill_grid(grid_visual, [4, 10]))
