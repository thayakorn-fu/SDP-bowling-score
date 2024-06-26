from .constants import MAX_FRAMES, STRIKE_SCORE, SPARE_SCORE


class Frame:
    def __init__(self, rolls):
        self.rolls = rolls

    def score(self):
        return sum(self.rolls)


class StrikeFrame(Frame):
    def score(self, next_two_rolls):
        return 10 + sum(next_two_rolls[:2])


class SpareFrame(Frame):
    def score(self, next_roll):
        # next_roll is the score of the next roll after the spare
        return 10 + next_roll


class LastFrame(Frame):
    def __init__(self, rolls):
        super().__init__(rolls)
        # Ensure rolls for LastFrame can accommodate up to 3 rolls
        if len(rolls) > 3:
            raise ValueError("LastFrame can have a maximum of 3 rolls")

    def score(self):
        # Simply sum up the rolls, as special scoring rules do not apply to the last frame
        return sum(self.rolls)


class FrameFactory:
    @staticmethod
    def create_frame(rolls, position):
        if position == MAX_FRAMES - 1:
            return LastFrame(rolls)
        elif rolls[0] == STRIKE_SCORE:
            return StrikeFrame(rolls)
        elif sum(rolls) == SPARE_SCORE:
            return SpareFrame(rolls)
        else:
            return Frame(rolls)


class BowlingScoreCalculator:
    def calculate_score(self, frames):
        total_score = 0
        for i, frame_rolls in enumerate(frames):
            frame = FrameFactory.create_frame(frame_rolls, i)
            # Assuming a method to calculate the score correctly based on frame type
            total_score += frame.score()
        return total_score
