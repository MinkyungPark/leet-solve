class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a
        
        def lcm(a: int, b: int) -> int:
            return a // gcd(a, b) * b
        
        # Inclusion-Exclusion Principle
        # |𝐴∪𝐵∪𝐶|=(|𝐴|+|𝐵|+|𝐶|)−(|𝐴∩𝐵|+|𝐵∩𝐶|+|𝐶∩𝐴|)+|𝐴∩𝐵∩𝐶|
        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(a, bc)

        def count(x):
            return (
                x // a + x // b + x // c
                - x // ab - x // ac - x // bc
                + x // abc
            )
        
        left = 1
        right = min(a,b,c) * n
        
        while left < right:
            mid = (left + right) // 2

            if count(mid) < n:
                left = mid + 1
            else:
                right = mid
        
        return left