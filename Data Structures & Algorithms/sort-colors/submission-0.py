class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]
        for i in nums:
            colors[i] += 1
        
        ind = 0
        for i in range(3):
            while colors[i]:
                colors[i] -= 1
                nums[ind] = i
                ind += 1

        