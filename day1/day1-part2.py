from typing import List
import logging

def load_lines_from_file() -> List[str]:
    with open('day1/input.txt') as f:
        return f.readlines()
    
def is_char_int(char: str) -> bool:
    return char in '0123456789'

def get_arrays_of_number_strings() -> List[List[str]]:
    strings = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    return [list(string) for string in strings]

def get_array_of_ten_ints() -> List[int]:
    return [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def part1() -> int:
    input = load_lines_from_file()
    word_array = get_arrays_of_number_strings()
    sum: int = 0

    first = None
    for line in input:
        first = None
        second = None
        pos = get_array_of_ten_ints()
        for char in line:
            selected: str = None
            if is_char_int(char):
                selected = char
                logging.debug(f'Found {selected}')
            else:
                found_str_num = False
                for i in range(0, 9):
                    if char == word_array[i][pos[i]]:
                        pos[i] += 1
                    elif char == word_array[i][0]:
                        # If there's not a match in an ongoing string, but the char matches
                        # the first char of the string, then we're the index from the start.
                        pos[i] = 1
                    else:
                        # There is no match at all, so reset.
                        pos[i] = 0
                    if len(word_array[i]) == (pos[i]):
                        logging.debug(f'Found {word_array[i]}')
                        selected = str(i + 1)
                        pos[i] = 0
                        found_str_num = True
                        logging.debug(f'Found {selected}')
                if not found_str_num:
                    continue
            
            if first is None:
                first = selected
            else:
                second = selected
        
        combined_num: str = None
        if (second is None):
            combined_num = first + first
            logging.debug(f'{first} + {first} = {combined_num}')
        else:
            if first is None:
                print('UNEXPECTED')
                exit(1)
            combined_num = first + second
            logging.debug(f'{first} + {second} = {combined_num}')
            
        sum += int(combined_num)
        first = None
        second = None
    
    return sum

logging.basicConfig(level=logging.ERROR)
print(f'Total is {part1()}')