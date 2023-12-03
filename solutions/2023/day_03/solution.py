# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/3

from ...base import TextSolution, answer
from itertools import groupby

LINE_LENGHT_TEST = len('467..114..')
LINE_LENGTH = len(
    '48.................501....33.....622..............763.........331.................161.683......................................980..........')


def get_number_at_(position: int, game_input: str) -> dict:
    if not game_input[position].isdigit():
        return {}
    else:
        number_string = game_input[position:position + 6].split('.')[0]
        number = ''
        for char_position in range(len(number_string)):
            if number_string[char_position].isdigit():
                number += number_string[char_position]
            else:
                break

        if number != '':
            return {'number': int(number), 'start': position, 'length': len(number)}
        else:
            return {}


def number_if_symbol_around(number_dict: dict, line_length: int, game_input: str) -> (int, dict):
    symbol_around = False

    start = number_dict['start']
    length = number_dict['length']

    for position in range(length):
        # left
        if (not game_input[start + position - 1] == '.'
                and not game_input[start + position - 1].isdigit()
                and not game_input[start + position - 1] == '\n'):
            symbol_around = {'symbol': game_input[start + position - 1], 'position': start + position - 1}
        # right
        elif (not game_input[start + position + 1] == '.'
              and not game_input[start + position + 1].isdigit()
              and not game_input[start + position + 1] == '\n'):
            symbol_around = {'symbol': game_input[start + position + 1], 'position': start + position + 1}
        # up
        elif (not start + position - line_length < 0
              and not game_input[start + position - line_length] == '.'
              and not game_input[start + position - line_length] == '\n'
              and not game_input[start + position - line_length].isdigit()):
            symbol_around = {'symbol': game_input[start + position - line_length],
                             'position': start + position - line_length}
        # down
        elif (not start + position + line_length > len(game_input)
              and not game_input[start + position + line_length] == '.'
              and not game_input[start + position + line_length] == '\n'
              and not game_input[start + position + line_length].isdigit()):
            symbol_around = {'symbol': game_input[start + position + line_length],
                             'position': start + position + line_length}
        # up-left
        elif (not start + position - line_length - 1 < 0
              and not game_input[start + position - line_length - 1] == '.'
              and not game_input[start + position - line_length - 1] == '\n'
              and not game_input[start + position - line_length - 1].isdigit()):
            symbol_around = {'symbol': game_input[start + position - line_length - 1],
                             'position': start + position - line_length - 1}
        # up-right
        elif (not start + position - line_length + 1 < 0
              and not game_input[start + position - line_length + 1] == '.'
              and not game_input[start + position - line_length + 1] == '\n'
              and not game_input[start + position - line_length + 1].isdigit()):
            symbol_around = {'symbol': game_input[start + position - line_length + 1],
                             'position': start + position - line_length + 1}
        # down-right
        elif (not start + position + line_length + 1 > len(game_input)
              and not game_input[start + position + line_length + 1] == '.'
              and not game_input[start + position + line_length + 1] == '\n'
              and not game_input[start + position + line_length + 1].isdigit()):
            symbol_around = {'symbol': game_input[start + position + line_length + 1],
                             'position': start + position + line_length + 1}
        # down-left
        elif (not start + position + line_length - 1 > len(game_input)
              and not game_input[start + position + line_length - 1] == '.'
              and not game_input[start + position + line_length - 1] == '\n'
              and not game_input[start + position + line_length - 1].isdigit()):
            symbol_around = {'symbol': game_input[start + position + line_length - 1],
                             'position': start + position + line_length - 1}

    if symbol_around:
        symbol_around['number'] = number_dict['number']
        return number_dict['number'], symbol_around
    else:
        return 0, {}


class Solution(TextSolution):
    _year = 2023
    _day = 3

    # @answer(1234)
    def part_1(self) -> int:
        number_detected = False
        numbers = list()
        game_input = self.input

        for index in range(len(game_input)):
            if not number_detected and game_input[index].isdigit():
                number_detected = True
                numbers.append(get_number_at_(index, self.input))
            if not game_input[index].isdigit():
                number_detected = False

        total = 0
        for number in numbers:
            value, _ = number_if_symbol_around(number, LINE_LENGTH + 1, game_input)
            total += value

        return total

    # @answer(1234)
    def part_2(self) -> int:
        number_detected = False
        numbers = list()
        game_input = self.input

        for index in range(len(game_input)):
            if not number_detected and game_input[index].isdigit():
                number_detected = True
                numbers.append(get_number_at_(index, self.input))
            if not game_input[index].isdigit():
                number_detected = False

        symbol_list = list()

        for number in numbers:
            _, symbol = number_if_symbol_around(number, LINE_LENGTH + 1, game_input)
            if symbol != {}:
                symbol_list.append(symbol)

        star_symbols = filter(lambda symbol_entry: symbol_entry['symbol'] == '*', symbol_list)
        star_symbols_positions_with_number = [(symbol['position'], symbol['number']) for symbol in star_symbols]
        list_of_twice = list()

        for _, grouped in groupby(sorted(star_symbols_positions_with_number, key=lambda ele: ele[0]), key=lambda ele: ele[0]):
            grouped_list = list(grouped)
            if len(grouped_list) == 2:
                list_of_twice.append(grouped_list)
        numbers_to_multiply = [(grouped[0][1], grouped[1][1]) for grouped in list_of_twice]

        result = 0
        for number_pair in numbers_to_multiply:
            result += number_pair[0] * number_pair[1]

        return result

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
