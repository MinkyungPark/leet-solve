class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # O(N) + k break constraint
        # cnt = 0

        # for i in range(1, n + 1):
        #     if n % i == 0:
        #         cnt += 1
        #         if cnt == k:
        #             return i
        
        # return -1
    
        # O(sqrt(N)) with factors d and n // d
        d = 1 # divisor
        small, large = [], []

        while d * d <= n:
            if n % d == 0:
                small.append(d)

                if d != (n // d): # dedup : 12 > 6 * 6
                    large.append(n // d)
        
            d += 1
        
        factors = small + large[::-1]
        if k > len(factors):
            return -1
        
        return factors[k - 1]
