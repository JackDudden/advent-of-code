import unittest
import calibrator


class TestCalibrator(unittest.TestCase):
    def test_basic_calibrate(self):
        input = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
        self.assertEqual(
            calibrator.calibrate(input, parse_words=False),
            142,
            "Example calibration should equal 142",
        )

    def test_parsed_calibrate(self):
        input = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ]
        self.assertEqual(
            calibrator.calibrate(input, parse_words=True),
            281,
            "Parsed calibbration should equal 281",
        )


if __name__ == "__main__":
    unittest.main()
