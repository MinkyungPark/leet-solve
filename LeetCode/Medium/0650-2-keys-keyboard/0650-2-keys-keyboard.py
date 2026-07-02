class Solution:
    def minSteps(self, n: int) -> int:
        # sum of prime factors
        # e.g. 15 = 5 * 3
        # step 5 : make 5
        # step 3 : cp5, ps5, ps5

        steps = 0
        i = 2
        while i * i <= n:
            while n % i == 0:
                steps += i
                n //= i
            i += 1

        if n > 1:
            steps += n

        return steps