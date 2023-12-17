import logging
from typing import List, Dict
import pprint
import re


def load_lines_from_file() -> List[str]:
    with open('day8/input.txt') as f:
        return f.readlines()


def get_ids(line: str) -> Dict:
    line = line.strip()
    match = re.search(
        r'([0-9A-Z]+) = \(([0-9A-Z]+), ([0-9A-Z]+)\)', line)
    if not match:
        print(f'line: {line} not found')
        return None
    return match.group(1), match.group(2), match.group(3)


lines = load_lines_from_file()

directions = list(lines[0].strip())

edges = {}
for i in range(2, len(lines)):
    key, left, right = get_ids(lines[i])
    edges[key] = {'L': left, 'R': right}

pprint.pprint(edges)

current_nodes = {k: v for k, v in edges.items() if k.endswith('A')}
count = 0
while not all(node.endswith('Z') for node in current_nodes):
    next_direction = directions[count % len(directions)]
    new_next = {}
    for node in current_nodes:
        next_val = edges[node][next_direction]
        new_next[next_val] = edges[next_val]
    current_nodes = new_next
    count += 1

print(count)
