"""
Advent of Code - Day 3
https://adventofcode.com/2023/day/3
"""

from engine import gear_ratios, part_numbers


def main() -> None:
    with open("input.txt", "r") as f:
        data = f.read()
    pnums = part_numbers(data)
    print(f"Part number sum: {sum(pnums)}")
    g_ratios = gear_ratios(data)
    print(f"Gear ration sum: {sum(g_ratios)}")
    return None


if __name__ == "__main__":
    main()
