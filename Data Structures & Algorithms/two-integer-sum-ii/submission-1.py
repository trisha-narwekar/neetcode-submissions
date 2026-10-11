class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1 
        result = []

        while (left < right):
            temp_sum = numbers[left] + numbers[right]
            if temp_sum == target:
                result = [numbers[left], numbers[right]]
                return [left + 1, right + 1]
            elif temp_sum < target:
                left += 1
            else:
                right -= 1