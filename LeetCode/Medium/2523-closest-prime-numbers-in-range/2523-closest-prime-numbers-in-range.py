from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False

        for i in range(2, int(right ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, right + 1, i):
                    sieve[j] = False

        prev = -1
        ans = [-1, -1]
        min_gap = float('inf')

        for num in range(left, right + 1):
            if sieve[num]:
                if prev != -1:
                    gap = num - prev

                    if gap < min_gap:
                        min_gap = gap
                        ans = [prev, num]

                    # Smallest possible gap between primes
                    if gap == 2:
                        return ans

                prev = num

        return ans