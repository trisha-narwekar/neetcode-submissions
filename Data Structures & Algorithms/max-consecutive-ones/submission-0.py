class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr_count = 0

        for i in nums:
            if i == 1:
                curr_count += 1
                if curr_count > max_ones:
                    max_ones = curr_count
            else:
                curr_count = 0
        return max_ones