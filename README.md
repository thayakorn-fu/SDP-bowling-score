# Bowling Score Calculator

This project contains a Python package `bowling` that provides a `Calculator` class for calculating the score of a bowling game. It also includes unit tests for the `Calculator` class.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/bowling-score-calc.git
   ```

2. Navigate to the project directory:

   ```bash
   cd bowling-score-calc
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To calculate the score of a bowling game, follow these steps:

1. Import the `Calculator` class from the `bowling.calculator` module:

   ```python
   from bowling.calculator import Calculator
   ```

2. Create an instance of the `Calculator` class:

   ```python
   calculator = Calculator()
   ```

3. Prepare the frames of the bowling game as a list of tuples. Each tuple represents a frame and contains three integers: the number of pins knocked down in the first roll, the number of pins knocked down in the second roll, and the number of bonus rolls (if any).

   ```python
   frames = [
       (10, 0, 0),  # Strike
       (7, 3, 0),   # Spare
       (4, 2, 0),   # Open frame
       (10, 0, 0),  # Strike
       (10, 0, 0),  # Strike
       (7, 2, 0),   # Open frame
       (9, 1, 0),   # Spare
       (10, 0, 0),  # Strike
       (10, 0, 0),  # Strike
       (10, 10, 10) # Strike with bonus rolls
   ]
   ```

4. Call the `calculate_score` method of the `Calculator` instance, passing the frames as an argument:

   ```python
   score = calculator.calculate_score(frames)
   ```

5. The `calculate_score` method will return the total score of the bowling game.

## Running the Tests

To run the unit tests for the `Calculator` class, use the following command:

```bash
python -m unittest tests.test_calculator
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.