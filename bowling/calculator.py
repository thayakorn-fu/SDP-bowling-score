from .constants import MAX_FRAMES, STRIKE_SCORE, SPARE_SCORE


class BowlingScoreCalculator:
    """
    A class to calculate the score of a single game of bowling.
    """

    def calculate_score(self, frames):
        """
        Calculate the total score for a given list of frames in a bowling game.

        Parameters:
        frames (list): A list of lists, where each inner list represents a frame and contains the number of pins knocked down in each roll.

        Returns:
        int: The total score of the game.
        """
        total_score = 0
        for frame_index in range(MAX_FRAMES):
            frame = frames[frame_index]
            if frame_index < 9:  # For frames 1-9
                # Normally, only consider the first two rolls
                if self.is_strike(frame):  # Strike
                    total_score += STRIKE_SCORE
                    total_score += self.get_strike_bonus(frames, frame_index)
                elif self.is_spare(frame):  # Spare
                    total_score += SPARE_SCORE + \
                        self.get_spare_bonus(frames, frame_index)
                else:
                    total_score += sum(frame)
            else:  # For the last frame
                # In the last frame, all rolls count directly
                total_score += sum(frame)
        return total_score

    def is_strike(self, frame):
        """
        Determine if a frame is a strike.

        Parameters:
        frame (list): The frame to check.

        Returns:
        bool: True if the frame is a strike, False otherwise.
        """
        return frame[0] == STRIKE_SCORE  # Placeholder for method implementation

    def is_spare(self, frame):
        """
        Determine if a frame is a spare.

        Parameters:
        frame (list): The frame to check.

        Returns:
        bool: True if the frame is a spare, False otherwise.
        """
        return sum(frame) == SPARE_SCORE

    def get_strike_bonus(self, frames, frame_index):
        """
        Calculate the bonus for a strike frame.

        Parameters:
        frames (list): A list of lists representing the frames of the game.
        frame_index (int): The index of the strike frame.

        Returns:
        int: The bonus points for the strike.
        """
        bonus = 0
        # For frames 1 to 9
        if frame_index < 8:  # Adjusted to exclude the 10th frame in this logic
            next_frame = frames[frame_index + 1]
            bonus += next_frame[0]  # Add the first roll of the next frame
            if next_frame[0] == 10:  # If the next frame is also a strike
                # Check if there's another frame after the next
                if frame_index + 2 < len(frames):
                    # Add the first roll of the frame after next
                    bonus += frames[frame_index + 2][0]
            else:
                if len(next_frame) > 1:  # If the next frame is not a strike, add the second roll
                    bonus += next_frame[1]
        # For the 10th frame, the bonus is already included in the frame's score
        elif frame_index == 8:
            return frames[frame_index + 1][0] + frames[frame_index + 1][1]
        return bonus

    def get_spare_bonus(self, frames, frame_index):
        """
        Calculate the bonus for a spare frame.

        Parameters:
        frames (list): A list of lists representing the frames of the game.
        frame_index (int): The index of the spare frame.

        Returns:
        int: The bonus points for the spare.
        """
        # Spare bonus is the number of pins knocked down in the first roll of the next frame
        if frame_index + 1 < len(frames):
            return frames[frame_index + 1][0]
        return 0
