# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/7

from ...base import TextSolution, answer
from functools import cmp_to_key

card_order_string = '23456789TJQKA'
card_order_string_jack = 'J23456789TQKA'

part2 = False


def cards_comparator(hand1, hand2):
    cards1: str = hand1[0]
    cards2: str = hand2[0]

    if part2 is False:
        for index, _ in enumerate(cards1):
            if card_order_string.index(cards1[index]) < card_order_string.index(cards2[index]):
                return -1
            elif card_order_string.index(cards1[index]) > card_order_string.index(cards2[index]):
                return 1
            else:
                continue
    else:
        for index, _ in enumerate(cards1):
            if card_order_string_jack.index(cards1[index]) < card_order_string_jack.index(cards2[index]):
                return -1
            elif card_order_string_jack.index(cards1[index]) > card_order_string_jack.index(cards2[index]):
                return 1
            else:
                continue


def is_full_house(counts):
    if part2 is True and counts.get('J') is not None:
        jack_count = counts.pop('J') if counts.get('J') is not None else 0
        if list(counts.values()).count(2) == 2 and jack_count == 1:
            return True
    else:
        counts = counts.values()

    return list(counts).count(2) == 1 and list(counts).count(3) == 1


def is_two_pairs(counts):
    return list(counts).count(2) == 2


def get_type_for_(biggest_pair, counts):
    if biggest_pair == 5:
        return "five_of_a_kind"
    elif biggest_pair == 4:
        return "four_of_a_kind"
    elif biggest_pair == 3:
        if is_full_house(counts):
            return "full_house"
        else:
            return "three_of_a_kind"
    elif biggest_pair == 2 and is_two_pairs(counts.values()):
        return "two_pair"
    elif biggest_pair == 2:
        return "one_pair"
    else:
        return "high_card"


def get_type(hand):
    cards: str = hand[0]
    counts: dict = {}
    for card in cards:
        counts[card] = cards.count(card)

    biggest_pair = max(counts.values())
    jack_count = counts.get('J')

    if part2 is True and jack_count is not None:
        old_counts = counts.copy()
        counts.pop('J')
        if jack_count == 5:
            biggest_pair = 5
        else:
            biggest_pair = max(counts.values()) + jack_count
        counts = old_counts

    return get_type_for_(biggest_pair, counts)


def attach_rank_to(hands):
    ranked_hands = []

    for hand in sorted(hands.get('high_card'), key=cmp_to_key(cards_comparator)):
        ranked_hands.append(hand)

    for hand in sorted(hands.get('one_pair'), key=cmp_to_key(cards_comparator)):
        ranked_hands.append(hand)

    for hand in sorted(hands.get('two_pair'), key=cmp_to_key(cards_comparator)):
        ranked_hands.append(hand)

    for hand in sorted(hands.get('three_of_a_kind'), key=cmp_to_key(cards_comparator)):
        ranked_hands.append(hand)

    for hand in sorted(hands.get('full_house'), key=cmp_to_key(cards_comparator)):
        ranked_hands.append(hand)

    for hand in sorted(hands.get('four_of_a_kind'), key=cmp_to_key(cards_comparator)):
        ranked_hands.append(hand)

    for hand in sorted(hands.get('five_of_a_kind'), key=cmp_to_key(cards_comparator)):
        ranked_hands.append(hand)

    total = 0
    for index, hand in enumerate(ranked_hands):
        total += (index + 1) * hand[1]

    return total


class Solution(TextSolution):
    _year = 2023
    _day = 7

    # @answer(1234)
    def part_1(self) -> int:
        hands_with_bids = []
        for entry in self.input.split('\n'):
            entries = entry.split(' ')
            hands_with_bids.append((entries[0], int(entries[1])))

        kinds: dict = {
            'five_of_a_kind': [],
            'four_of_a_kind': [],
            'full_house': [],
            'three_of_a_kind': [],
            'two_pair': [],
            'one_pair': [],
            'high_card': []
        }

        for hand in hands_with_bids:
            hand_type = get_type(hand)
            newEntry = kinds.get(hand_type)
            newEntry.append(hand)
            kinds[hand_type] = newEntry

        return attach_rank_to(kinds)

    # @answer(1234)
    def part_2(self) -> int:
        global part2
        part2 = True

        hands_with_bids = []
        for entry in self.input.split('\n'):
            entries = entry.split(' ')
            hands_with_bids.append((entries[0], int(entries[1])))

        kinds: dict = {
            'five_of_a_kind': [],
            'four_of_a_kind': [],
            'full_house': [],
            'three_of_a_kind': [],
            'two_pair': [],
            'one_pair': [],
            'high_card': []
        }

        for hand in hands_with_bids:
            hand_type = get_type(hand)
            newEntry = kinds.get(hand_type)
            newEntry.append(hand)
            kinds[hand_type] = newEntry

        return attach_rank_to(kinds)

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
