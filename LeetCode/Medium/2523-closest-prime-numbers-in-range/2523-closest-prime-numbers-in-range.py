class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = bytearray(b'\x01') * (right + 1)
        is_prime[0] = is_prime[1] = 0

        for i in range(2, int(right ** 0.5) + 1):
            if is_prime[i]:
                for m in range(i * i, right + 1, i):
                    is_prime[m] = 0
        
        res = [-1, -1]
        prime = -1
        min_diff = right - left + 1

        for n in range(left, right + 1):
            if not is_prime[n]:
                continue
            
            if prime != -1:
                diff = n - prime

                if diff < min_diff:
                    res = [prime, n]
                
                if diff <= 2:
                    return res
            
            prime = n
        
        return res