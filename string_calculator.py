# string_calculator.py

import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter = ",|\n"
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = re.escape(parts[0][2:])
            numbers = parts[1]

        number_list = re.split(delimiter, numbers)
        sum = 0
        negatives = []

        for number in number_list:
            if number:
                num = int(number)
                if num < 0:
                    negatives.append(num)
                sum += num

        if negatives:
            raise ValueError(f"negative numbers not allowed {', '.join(map(str, negatives))}")

        return sum
