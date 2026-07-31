class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_pairs = sorted(
            enumerate(nums),
            key=lambda pair: pair[1]
        )
        s, e = 0, len(nums) - 1

        while s < e:
            if sorted_pairs[s][1] + sorted_pairs[e][1] > target:
                e -= 1
            elif sorted_pairs[s][1] + sorted_pairs[e][1] < target:
                s += 1
            else:
                return [sorted_pairs[s][0], sorted_pairs[e][0]]

