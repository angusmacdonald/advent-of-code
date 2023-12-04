from typing import List


def load_lines_from_file() -> List[str]:
    with open('day4/input.txt') as f:
        return f.readlines()


def parse_file(lines: List[str]) -> List[int]:
    count_list: List[int] = [0] * len(lines)
    print(count_list)

    for x in range(0, len(lines)):
        print(f'line[{x}]')
        line = lines[x]
        line = line[line.index(':')+2:]
        winners, selected = line.split(' | ')
        winners = winners.replace('  ', ' ').strip().lstrip()
        selected = selected.replace('  ', ' ').strip().lstrip()

        winners_list = winners.split(' ')
        selected_list = selected.split(' ')

        winners_list = [int(i) for i in winners_list]
        selected_list = [int(i) for i in selected_list]

        num_won = 0
        for i in range(0, len(selected_list)):
            if selected_list[i] in winners_list:
                num_won += 1

        count_list[x] += 1

        for j in range(x+1, min(x+num_won+1, len(count_list))):
            count_list[j] += count_list[x]

        print(f'num_won: {num_won} count_list[{x}]: {count_list}')

    print(count_list)
    return count_list


lines = load_lines_from_file()
print(sum(parse_file(lines)))
