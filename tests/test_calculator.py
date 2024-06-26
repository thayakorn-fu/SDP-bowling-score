import unittest
from bowling.calculator import BowlingScoreCalculator


class TestCalculator(unittest.TestCase):
    def test_all_gutter_balls(self):
        calculator = BowlingScoreCalculator()
        frames = [(0, 0)] * 10
        expected_score = 0
        self.assertEqual(calculator.calculate_score(frames), expected_score)

    def test_all_strikes(self):
        calculator = BowlingScoreCalculator()
        frames = [(10, 0)] * 9
        # 10th frame with 3 rolls, all strikes
        frames.append((10, 10, 10))
        expected_score = 300
        self.assertEqual(calculator.calculate_score(frames), expected_score)

    def test_all_spares(self):
        calculator = BowlingScoreCalculator()
        # Corrected to include a single bonus roll of 5 pins
        frames = [(5, 5)] * 9
        frames.append((5, 5, 5))
        expected_score = 150
        self.assertEqual(calculator.calculate_score(frames), expected_score)

    def test_random_frames(self):
        calculator = BowlingScoreCalculator()
        frames = [(1, 4), (4, 5), (6, 4), (5, 5), (10, 0),
                  (0, 1), (7, 3), (6, 4), (10, 0), (2, 8, 6)]
        expected_score = 133
        self.assertEqual(calculator.calculate_score(frames), expected_score)


if __name__ == '__main__':
    unittest.main()
