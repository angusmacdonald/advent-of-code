from typing import List, Dict
import collections
import sys
import common
from tqdm import tqdm


def get_sum_of_row(grid: List[List[str]], row: int) -> int:
    return sum([1 for c in grid[row] if c == '#'])


def get_sum_of_column(grid: List[List[str]], column: int) -> int:
    return sum([1 for row in grid if row[column] == '#'])


def get_sum_of_rows_and_columns(grid: List[List[str]]) -> Dict[int, int]:
    return {
        'rows': [get_sum_of_row(grid, row) for row in range(len(grid))],
        'columns': [get_sum_of_column(grid, column) for column in range(len(grid[0]))]
    }


def create_new_grid(grid: List[List[str]], new_rows: int, new_columns: int, sum_of_rows_and_cols: Dict[int, int]) -> List[List[str]]:
    new_grid = []

    new_x_length = len(grid[0]) + new_columns
    y_counts = sum_of_rows_and_cols["rows"]
    x_counts = sum_of_rows_and_cols["columns"]

    for y in range(len(grid)):
        if y_counts[y] == 0:
            new_grid.append(['.'] * new_x_length)
            new_grid.append(['.'] * new_x_length)
        else:
            new_row = []
            for x in range(len(grid[y])):
                if grid[y][x] == '#':
                    new_row.append('#')
                elif x_counts[x] == 0:
                    new_row.append('.')
                    new_row.append('.')
                else:
                    new_row.append('.')
            new_grid.append(new_row)
    return new_grid


def bfs(grid, start, destination):
    width, height = len(grid[0]), len(grid)
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        y, x = path[-1]
        if (y, x) == destination:
            return path
        for y2, x2 in ((y, x+1), (y, x-1), (y+1, x), (y-1, x)):
            if 0 <= x2 < width and 0 <= y2 < height and (y2, x2) not in seen:
                queue.append(path + [(y2, x2)])
                seen.add((y2, x2))


def find_positions_of_hashes(grid: List[List[str]]) -> List[Dict[int, int]]:
    return [(y, x) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == '#']


grid = common.parse_grid_from_file('day11/test.txt')
sum_of_rows_and_cols = get_sum_of_rows_and_columns(grid)
new_rows = sum([1 for row in sum_of_rows_and_cols["rows"] if row == 0])
new_cols = sum([1 for row in sum_of_rows_and_cols["columns"] if row == 0])

new_grid = create_new_grid(grid, new_rows, new_cols, sum_of_rows_and_cols)

positions = find_positions_of_hashes(new_grid)
print(f'positions length: {len(positions)}')
sum = 0
counted = 0


with tqdm(total=(len(positions)*len(positions)-len(positions))/2) as pbar:
    for pos in positions:
        for other_pos in positions:
            if pos == other_pos or other_pos < pos:
                continue
            path = bfs(new_grid, pos, other_pos)
            sum += (len(path)-1)
            counted += 1
            pbar.update(1)

print(f'sum: {sum}')
