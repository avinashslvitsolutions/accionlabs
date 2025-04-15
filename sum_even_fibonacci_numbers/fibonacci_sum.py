class EvenFibonacciCalculator:

    def __init__(self, count):
        """
        Initializes the calculator with the number of even Fibonacci numbers to sum.
        """
        self.count = count

    def generate_even_fibonacci(self):
        """
        Generates the first `count` even Fibonacci numbers.

        Returns:
            list: A list containing the first `count` even Fibonacci numbers.
        """
        even_fibs = []
        a, b = 0, 2  # First two even Fibonacci numbers

        while len(even_fibs) < self.count:
            even_fibs.append(b)
            a, b = b, 4 * b + a

        return even_fibs

    def sum_even_fibonacci(self):
        """
        Calculates the sum of the first `count` even Fibonacci numbers.
        """
        even_fibs = self.generate_even_fibonacci()
        return sum(even_fibs)


def main():
    """
    Main function to create the calculator and print the result.
    """
    count = 100  # first 100 even-valued Fibonacci numbers
    calculator = EvenFibonacciCalculator(count)
    total_sum = calculator.sum_even_fibonacci()
    print(f"Sum of the first {count} even Fibonacci numbers: {total_sum}")


if __name__ == "__main__":
    main()

