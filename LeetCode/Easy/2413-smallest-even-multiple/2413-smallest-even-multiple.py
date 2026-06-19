class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        a, b = 2, n
        
        while b != 0:
            a, b = b, a % b
        gcd = a

        return n // gcd * 2
