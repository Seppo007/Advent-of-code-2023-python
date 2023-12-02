# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template
import functools

# puzzle prompt: https://adventofcode.com/2023/day/2

from ...base import TextSolution, answer

MAX_RED_CUBES = 12
MAX_GREEN_CUBES = 13
MAX_BLUE_CUBES = 14


def get_cube_combinations_list(game: str) -> list:
    cube_combinations_str = game.split(': ', )[1]
    return cube_combinations_str.split('; ')


def get_game_id_for_(game: str) -> int:
    return int((game.split(':')[0])[5:])


def get_cube_count_from_(tuple: str) -> int:
    return int(tuple[:2] if tuple[1].isdigit() else tuple[0])


def get_game_id_if_no_combination_violates_ranges(game: str) -> int:
    red, green, blue = 0, 0, 0
    for comb in get_cube_combinations_list(game):
        cube_tuple_string_list = comb.split(', ')
        for cube_tuple_string in cube_tuple_string_list:
            if cube_tuple_string.__contains__('red'):
                red = get_cube_count_from_(cube_tuple_string)
            elif cube_tuple_string.__contains__('green'):
                green = get_cube_count_from_(cube_tuple_string)
            else:
                blue = get_cube_count_from_(cube_tuple_string)

            if red > MAX_RED_CUBES or green > MAX_GREEN_CUBES or blue > MAX_BLUE_CUBES:
                return 0

    return get_game_id_for_(game)


class Solution(TextSolution):
    _year = 2023
    _day = 2

    # @answer(1234)
    def part_1(self) -> int:
        id_count = 0
        games_list = self.input.split('\n')
        for game in games_list:
            id_count += get_game_id_if_no_combination_violates_ranges(game)

        return id_count

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
