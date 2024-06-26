import unittest
from bowling.frame import Frame


class TestFrame(unittest.TestCase):
    def test_frame_initialization(self):
        frame = Frame([5, 4])
        self.assertEqual(frame.rolls, [5, 4])

    def test_normal_scoring(self):
        frame = Frame([3, 6])
        self.assertEqual(frame.score(), 9)

    def test_spare_scoring(self):
        frame = Frame([7, 3], next_roll=5)
        self.assertEqual(frame.score(), 15)

    def test_strike_scoring(self):
        frame = Frame([10], next_two_rolls=[10, 3])
        self.assertEqual(frame.score(), 23)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            Frame([11])


if __name__ == '__main__':
    unittest.main()
