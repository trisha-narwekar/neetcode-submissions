class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sliding window
        # create set
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check for start
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest