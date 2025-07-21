class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False  # Ugly numbers are positive

        # Divide n by 2, 3, and 5 until it's no longer divisible
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        # If n becomes 1, it has no prime factors other than 2, 3, 5
        return n == 1
            