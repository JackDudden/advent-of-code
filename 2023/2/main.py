"""
Advent of Code - Day 2
https://adventofcode.com/2023/day/2
"""

from game import Match, Bag


def main() -> None:
    with open("input.txt", "r") as f:
        data = f.read()

    match = Match.loadstr(data)
    bag = Bag({"red": 12, "blue": 14, "green": 13})
    print(f"Match score: {match.score(bag)}")
    print(f"Match power: {match.power()}")
    return None


if __name__ == "__main__":
    main()
