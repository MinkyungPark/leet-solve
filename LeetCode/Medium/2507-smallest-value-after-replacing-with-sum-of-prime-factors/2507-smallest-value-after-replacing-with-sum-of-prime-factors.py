class Solution:
    def smallestValue(self, n: int) -> int:
        
        def get_primes(x):
            primes = []

            i = 2
            while i * i <= x:
                while x % i == 0:
                    primes.append(i)
                    x //= i
                i += 1
            
            if x > 1:
                primes.append(x)
            
            return primes

        while True:
            new_n = sum(get_primes(n))
            if n == new_n:
                break
            n = new_n
        
        return n
