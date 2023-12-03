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

def is_valid_game(game_rounds, max_blue, max_red, max_green) -> bool:
    for round in game_rounds:
        if int(round['green']) > max_green:
            return False
        if int(round['red']) > max_red:
            return False
        if int(round['blue']) > max_blue:
            return False
    return True

def part2(max_blue, max_red, max_green) -> int:
    input = load_lines_from_file()
    
    total_valid = 0
    for line in input:
        game_number, game_rounds = parse_line(line)
        if is_valid_game(game_rounds, max_blue, max_red, max_green):
         total_valid +=game_number
    return total_valid


print(part2(max_blue=14,max_red=12,max_green=13))