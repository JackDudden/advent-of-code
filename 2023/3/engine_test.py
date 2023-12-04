"""
Advent of Code - Day 3
https://adventofcode.com/2023/day/3
"""

import unittest
from engine import gear_ratios, part_numbers


class TestPartNumbers(unittest.TestCase):
    def test_part_numbers(self):
        schematic = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
        self.assertEqual(
            part_numbers(schematic),
            [467, 35, 633, 617, 592, 755, 664, 598],
            "Part numbers not all found",
        )

    def test_part_sum(self):
        schematic = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
        self.assertEqual(
            sum(part_numbers(schematic)),
            4361,
            "Part numbers not summed correctly",
        )

    def test_gear_ratios(self):
        schematic = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
        self.assertEqual(
            gear_ratios(schematic), [16345, 451490], "Gear ratios not all found"
        )

    def test_gear_sum(self):
        schematic = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
        self.assertEqual(
            sum(gear_ratios(schematic)), 467835, "Gear ratios sum incorrect"
        )


if __name__ == "__main__":
    unittest.main()
