"""
Advent of Code - Day 3
https://adventofcode.com/2023/day/3
"""

from functools import reduce
import re
import string
import operator


def part_numbers(schematic: str) -> list[int]:
    """
    Finds all part numbers associated with a schematic.
    """
    numbers = find_by_regex(schematic, r"\d+")
    symbols = find_by_regex(
        schematic, "|".join(re.escape(sym) for sym in string.punctuation if sym != ".")
    )
    part_nums = [
        int(x[0])
        for x in filter(
            lambda x: any(check_adjacent(x, symbol) for symbol in symbols), numbers
        )
    ]
    return part_nums


def gear_ratios(schematic: str) -> list[int]:
    """
    Finds all the gear ratios associated with a schematic.
    """
    numbers = find_by_regex(schematic, r"\d+")
    gears = find_by_regex(schematic, r"\*")
    gear_combos = [
        [int(num[0]) for num in numbers if check_adjacent(num, gear)] for gear in gears
    ]
    gear_pairs = filter(lambda x: len(x) == 2, gear_combos)
    return [reduce(operator.mul, pair, 1) for pair in gear_pairs]


def find_by_regex(schematic: str, regex: str):
    """
    Finds all numbers in a schematic and for each returns the number
    as a string, it's line position, and it's column position in a list.
    """
    store = []
    for i, line in enumerate(schematic.splitlines()):
        for match in re.finditer(regex, line):
            store.append([match.group(), i, match.start()])

    return store


def check_adjacent(number, sym):
    """
    Checks a numbers position against the list of symbols.
    """
    check_horizontal = number[2] - 1 <= sym[2] <= number[2] + len(number[0])
    check_vertical = number[1] - 1 <= sym[1] <= number[1] + 1
    if check_horizontal and check_vertical:
        return True

    return False
