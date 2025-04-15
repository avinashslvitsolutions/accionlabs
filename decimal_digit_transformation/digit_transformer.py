class DigitTransformer:
    """
    A class that transforms a single digit into the sum of its sequence:
    """
    
    def __init__(self, digit: int):
        """
        Initialize the transformer with a digit.
        """
        self._validate_digit(digit)
        self.digit = digit
        self.result = None
    
    def _validate_digit(self, digit):
        """Validate that input is a single decimal digit."""
        if not isinstance(digit, int):
            raise ValueError("Input must be an integer")
        if not 0 <= digit <= 9:
            raise ValueError("Input must be a single digit (0-9)")
    
    def calculate(self) -> int:
        """
        Calculate the transformation sum: X + XX + XXX + XXXX
            If digit is 3, returns 3702 (3 + 33 + 333 + 3333)
        """
        if self.result is not None:
            return self.result
            
        terms = [
            self.digit,
            self.digit * 11,
            self.digit * 111,
            self.digit * 1111
        ]
        self.result = sum(terms)
        return self.result
    
    def get_result(self) -> int:
        """
        Get the calculated result. Will calculate if not already done.
        """
        if self.result is None:
            self.calculate()
        return self.result


def get_user_input() -> int:
    """
    Helper function to get and validate user input.
    
    """
    while True:
        try:
            user_input = input("Enter a single digit (0-9): ")
            digit = int(user_input)
            if not 0 <= digit <= 9:
                raise ValueError("Please enter a single digit (0-9)")
            return digit
        except ValueError as e:
            print(f"Invalid input: {e}")


if __name__ == "__main__":
    print("Digit Transformation Calculator")
    
    try:
        # Get user input
        digit = get_user_input()
        
        # Calculate and display result
        transformer = DigitTransformer(digit)
        result = transformer.get_result()
        
        print(f"\nCalculation for digit {digit}:")
        print(f"{digit} + {digit}{digit} + {digit}{digit}{digit} + {digit}{digit}{digit}{digit} = {result}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
