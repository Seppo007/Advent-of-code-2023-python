# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/6

from ...base import TextSolution, answer

class Solution(TextSolution):
    _year = 2023
    _day = 6

    # @answer(1234)
    def part_1(self) -> int:
        clearedInput = self.input.split()
        entriesCount = int(len(self.input.split()) / 2)

        pairs = []
        for i in range(1, entriesCount):
            pairs.append((int(clearedInput[i]), int(clearedInput[i + entriesCount])))

        print("pairs:", pairs)

        total = 1
        for pair in pairs:
            recordBeatWays = 0
            time = pair[0]
            for i in range(1, time):
                recordBeatWays += 1 if (i * (time - i)) > pair[1] else 0
            total *= recordBeatWays

        return total

        # @answer(1234)
    def part_2(self) -> int:
        clearedInput = self.input.split()
        time = int(''.join(clearedInput[1:int(len(clearedInput)/2)]))
        distance = int(''.join(clearedInput[int(len(clearedInput)/2)+1:]))

        recordBeatWays = 0
        for i in range(1, time):
            recordBeatWays += 1 if (i * (time - i)) > distance else 0

        return recordBeatWays

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
