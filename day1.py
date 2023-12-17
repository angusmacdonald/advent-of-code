from typing import List

def load_lines_from_file() -> List[str]:
    with open('day1/input.txt') as f:
        return f.readlines()
    
def is_char_int(char: str) -> bool:
    return char in '0123456789'

def part1() -> int:
    input = load_lines_from_file()

    sum: int = 0

    first = None
    for line in input:
        first = None
        second = None
        for char in line:
            if not is_char_int(char):
                continue
            
            if first is None:
                first = char
            else:
                second = char
        
        combined_num: str = None
        if (second is None):
            combined_num = first + first
            print(f'{first} + {first} = {combined_num}')
        else:
            if first is None:
                print('UNEXPECTED')
                exit(1)
            combined_num = first + second
            print(f'{first} + {second} = {combined_num}')
            
        sum += int(combined_num)
        first = None
        second = None
    
    return sum


print(part1())