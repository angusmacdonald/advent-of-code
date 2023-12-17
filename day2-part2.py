from typing import List
import re


def load_lines_from_file() -> List[str]:
    with open('day2/input.txt') as f:
        return f.readlines()
    
def get_num_of_color(color: str, line: str) -> int:
    match = re.search(r'(\d+) ' + color, line)
    if match:
        return int(match.group(1))
    return 0
        
def parse_line(game_string: str) -> [int, List[dict]]:
    match = re.search(r'Game (\d+):.*', game_string)
    game_number = match.group(1)
    
    print(f'Game number: {game_number}')

    broken_down_by_round = game_string[(len('Game : ') + len(str(game_number))):].split('; ')

    results = []
    for result in broken_down_by_round:
        num_green = get_num_of_color('green', result)   
        num_red = get_num_of_color('red', result)
        num_blue = get_num_of_color('blue', result)
        
        results.append({'green': num_green, 'red': num_red, 'blue': num_blue})
    
    return int(game_number), results

def min_required(game_rounds) -> bool:
    max_blue, max_red, max_green = 0, 0, 0
    for round in game_rounds:
        if round['green'] > max_green:
            max_green = round['green']
        if round['red'] > max_red:
            max_red =  round['red']
        if round['blue'] > max_blue:
           max_blue = round['blue']
    return max_blue * max_red * max_green

def part2() -> int:
    input = load_lines_from_file()
    
    total = 0
    for line in input:
        _, game_rounds = parse_line(line)
        total += min_required(game_rounds)
    return total


print(part2())