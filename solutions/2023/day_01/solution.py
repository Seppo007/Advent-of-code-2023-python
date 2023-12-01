# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/1

from ...base import TextSolution, answer

def concat_two_strings_to_int(string1: str, string2: str) -> int:
    return int(string1 + string2)

def get_concat_value_of_first_and_last_digit_in_(line: str) -> int:
    first = -1
    second = -1

    for character in line:
        if character.isdigit():
            if first == -1:
                first = character
            else:
                second = character

    return concat_two_strings_to_int(first, second) \
        if str(second) != str('-1') \
        else concat_two_strings_to_int(first, first)


def get_concat_value_of_first_and_last_numerical_in_(line: str) -> int:
    first = -1
    second = -1

    for index in range(0, len(line)):
        number = extract_numerical_or_digit_for_(line[index:])
        if number != '':
            if first == -1:
                first = number
            else:
               second = number

    return concat_two_strings_to_int(first, second) \
        if str(second) != str('-1') \
        else concat_two_strings_to_int(first, first)


def extract_numerical_or_digit_for_(string: str) -> str:
    if string[0].isdigit():
        return string[0]

    if string.startswith('one'):
        return '1'
    elif string.startswith('two'):
        return '2'
    elif string.startswith('three'):
        return '3'
    elif string.startswith('four'):
        return '4'
    elif string.startswith('five'):
        return '5'
    elif string.startswith('six'):
        return '6'
    elif string.startswith('seven'):
        return '7'
    elif string.startswith('eight'):
        return '8'
    elif string.startswith('nine'):
        return '9'
    elif string.startswith('zero'):
        return '0'
    else:
        return ''

class Solution(TextSolution):
    _year = 2023
    _day = 1

    # @answer(1234)
    def part_1(self) -> int:
        value = 0
        for line in self.input.split('\n'):
            value += get_concat_value_of_first_and_last_digit_in_(line)
        return value

    # @answer(1234)
    def part_2(self) -> int:
        value = 0
        for line in self.input.split('\n'):
            value += get_concat_value_of_first_and_last_numerical_in_(line)
        return value

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
