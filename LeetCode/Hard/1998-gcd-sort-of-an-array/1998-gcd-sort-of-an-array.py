# can swap if gcd(nums[i], nums[j]) > 1
# union among prime factors

class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        max_num = max(nums)
        parent = list(range(max_num + 1))
        spf = list(range(max_num + 1))

        for i in range(2, int(max_num ** 0.5) + 1):
            if spf[i] == i:
                for multiple in range(i * i, max_num + 1, i):
                    if spf[multiple] != multiple:
                        continue
                    spf[multiple] = i
        
        def prime_factors(x):
            factors = []

            while x > 1:
                factor = spf[x]
                factors.append(factor)

                while x % factor == 0:
                    x //= factor
            
            return factors

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                parent[root_b] = root_a

        for num in nums:
            for factor in prime_factors(num):
                union(num, factor)

        sorted_nums = sorted(nums)

        for i, j in zip(nums, sorted_nums):
            if find(i) != find(j):
                return False
        
        return True