"""
Advent of Code - Day 1
https://adventofcode.com/2023/day/1
"""

import calibrator


def main() -> None:
    with open("input.txt", "r") as f:
        doc1 = f.read().splitlines()
    cal1 = calibrator.calibrate(doc1, parse_words=False)
    print(f"Part 1 Calibration Value: {cal1}")
    cal2 = calibrator.calibrate(doc1, parse_words=True)
    print(f"Part 2 Calibration Value: {cal2}")
    return None


if __name__ == "__main__":
    main()
