class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 2
        first = nums[0]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < first:
                right = mid - 1
            else:
                left = mid + 1
        return first