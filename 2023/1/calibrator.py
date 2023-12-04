"""
Advent of Code - Day 1
https://adventofcode.com/2023/day/1
"""


def calibrate(document: list[str], parse_words: bool = True) -> int:
    """
    Takes a calibration document and returns the calibration value.
    """
    if parse_words:
        document = list(map(transform, document))
    digits = map(lambda x: list(filter(str.isdigit, x)), document)
    val = sum(map(lambda x: int(x[0] + x[-1]), digits))
    return val


def transform(line: str):
    """ """
    table = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }
    for k, v in table.items():
        line = line.replace(k, v)
    return line
