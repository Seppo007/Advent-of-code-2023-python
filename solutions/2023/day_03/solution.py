# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/3

from ...base import TextSolution, answer

LINE_LENGHT_TEST = len('467..114..')
LINE_LENGTH = len('48.................501....33.....622..............763.........331.................161.683......................................980..........')


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


def number_if_symbol_around(number_dict: dict, line_length: int, game_input: str) -> int:
    symbol_around = False

    start = number_dict['start']
    length = number_dict['length']

    for position in range(length):
        # left
        if (not game_input[start + position - 1] == '.'
                and not game_input[start + position - 1].isdigit()
                and not game_input[start + position - 1] == '\n'):
            symbol_around = True
        # right
        elif (not game_input[start + position + 1] == '.'
              and not game_input[start + position + 1].isdigit()
              and not game_input[start + position + 1] == '\n'):
            symbol_around = True
        # up
        elif (not start + position - line_length < 0
              and not game_input[start + position - line_length] == '.'
              and not game_input[start + position - line_length] == '\n'
              and not game_input[start + position - line_length].isdigit()):
            symbol_around = True
        # down
        elif (not start + position + line_length > len(game_input)
              and not game_input[start + position + line_length] == '.'
              and not game_input[start + position + line_length] == '\n'
              and not game_input[start + position + line_length].isdigit()):
            symbol_around = True
        # up-left
        elif (not start + position - line_length - 1 < 0
              and not game_input[start + position - line_length - 1] == '.'
              and not game_input[start + position - line_length - 1] == '\n'
              and not game_input[start + position - line_length - 1].isdigit()):
            symbol_around = True
        # up-right
        elif (not start + position - line_length + 1 < 0
              and not game_input[start + position - line_length + 1] == '.'
              and not game_input[start + position - line_length + 1] == '\n'
              and not game_input[start + position - line_length + 1].isdigit()):
            symbol_around = True
        # down-right
        elif (not start + position + line_length + 1 > len(game_input)
              and not game_input[start + position + line_length + 1] == '.'
              and not game_input[start + position + line_length + 1] == '\n'
              and not game_input[start + position + line_length + 1].isdigit()):
            symbol_around = True
        # down-left
        elif (not start + position + line_length - 1 > len(game_input)
              and not game_input[start + position + line_length - 1] == '.'
              and not game_input[start + position + line_length - 1] == '\n'
              and not game_input[start + position + line_length - 1].isdigit()):
            symbol_around = True

    if symbol_around:
        return number_dict['number']
    else:
        return 0



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
            total += number_if_symbol_around(number, LINE_LENGTH + 1, game_input)

        return total

    # @answer(1234)
    def part_2(self) -> int:
        return -2

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
