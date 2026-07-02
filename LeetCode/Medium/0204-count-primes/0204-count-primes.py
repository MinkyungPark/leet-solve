class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        # Eratosthenes'sieve 
        # log log 5,000,000 ≈ log(15.42) ≈ 2.73
        # n log log n = 5,000,000 * 2.73 ≈ 13,650,000
        
        is_prime = bytearray(b'\x01') * n
        is_prime[0] = 0
        is_prime[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, n, i):
                    is_prime[multiple] = 0

        return sum(is_prime)