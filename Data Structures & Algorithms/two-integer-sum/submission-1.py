class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in lookup:
                return [lookup[x], i]
            lookup[num] = i