import logging
from typing import List
import pprint


hand_index = ['J', '2', '3', '4', '5', '6',
              '7', '8', '9', 'T', 'Q', 'K', 'A']


def load_lines_from_file() -> List[str]:
    with open('day7/input.txt') as f:
        return f.readlines()


def get_line_pairs(list: List[str]) -> List[List[str]]:
    list_of_pairs = []
    for i in range(len(list)):
        hand, number = list[i].strip().split(' ')
        list_of_pairs.append([hand, int(number)])
    return list_of_pairs


def get_score_array(hand: str) -> List[int]:
    pos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for card in hand:
        pos[hand_index.index(card)] += 1

    return pos


def get_hand_score(hand: List[int]) -> int:

    if 5 in hand:
        return 100  # Five of a kind
    if 4 in hand:
        return 90  # Four of a kind
    if 3 in hand and 2 in hand:
        return 80  # Full house
    if 3 in hand:
        return 70  # Three of a kind
    if hand.count(2) == 2:
        return 60  # Two pair
    if 2 in hand:
        return 50  # One pair

    return 0  # High card


def get_wildcard_hand_score(hand: List[int]) -> int:
    joker = hand[0]
    if joker == 0:
        return get_hand_score(hand)

    max_score = 0
    for i in range(1, len(hand_index)):
        new_hand = hand.copy()
        new_hand[0] = 0
        new_hand[i] += joker
        new_score = get_hand_score(new_hand)
        if new_score > max_score:
            max_score = new_score

    return max_score


def get_hand_ordering(hand: str) -> int:
    multiplier = 10

    result = 0
    for i in range(len(hand)):
        next = len(hand) - i - 1
        result += hand_index.index(hand[next]) * multiplier
        multiplier *= 100

    return result


pairs = get_line_pairs(load_lines_from_file())

scored_pairs = []
for pair in pairs:
    array = get_score_array(pair[0])
    scored_pairs.append(
        {'score': get_wildcard_hand_score(array),
         'ordering': get_hand_ordering(pair[0]),
         'bet': pair[1],
         'hand': pair[0]})

# sort scored pairs by score, then ordering
scored_pairs.sort(key=lambda x: (x['score'], x['ordering']), reverse=False)

score = 0

for i in range(len(scored_pairs)):
    print(f'{i}: {scored_pairs[i]} {i+1}')
    score += scored_pairs[i]['bet'] * (i + 1)

# pprint.pprint(scored_pairs)
print(score)
