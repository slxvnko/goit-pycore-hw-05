import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Extracts all valid float numbers from text and yields them as a generator.
    Assumes numbers are clearly separated by spaces.
    """
    # Regular expression for valid floats
    pattern = r'\b\d+\.\d+|\b\d+\b'
    matches = re.findall(pattern, text)

    for number in matches:
        yield float(number)


def sum_profit(text: str, func: Callable) -> float:
    """
    Sums all numbers returned by generator_numbers.
    """
    return sum(func(text))


# Example usage:
text = (
    "An employee's total income consists of several parts: "
    "1000.01 as main income, supplemented by additional income "
    "27.45 and 324.00 dollars."
)

total_income = sum_profit(text, generator_numbers)
print(f"Actual income: {total_income}")  # 1351.46