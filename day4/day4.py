from typing import List


def load_lines_from_file() -> List[str]:
    with open('day4/input.txt') as f:
        return f.readlines()


def parse_line(line: str) -> dict:
    """Parse a line of the form 'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53'"""
    line = line[line.index(':')+2:]
    # split by | character
    winners, selected = line.split(' | ')
    winners = winners.replace('  ', ' ').strip().lstrip()
    selected = selected.replace('  ', ' ').strip().lstrip()

    winners_list = winners.split(' ')
    selected_list = selected.split(' ')

    winners_list = [int(i) for i in winners_list]
    selected_list = [int(i) for i in selected_list]
    print(winners_list)
    print(selected_list)

    sum = 0
    for i in range(0, len(selected_list)):
        if selected_list[i] in winners_list:
            if sum == 0:
                sum = 1
            else:
                sum *= 2

    return sum


lines = load_lines_from_file()
total = 0
for line in lines:
    total += parse_line(line)
print(total)
