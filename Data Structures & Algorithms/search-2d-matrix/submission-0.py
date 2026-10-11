class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix)) * (len(matrix[0])) - 1

        while left <= right:
            mid = (left + right) // 2
            midRow = mid // (len(matrix[0]))
            midCol = mid % (len(matrix[0]))
            
            if matrix[midRow][midCol] == target:
                return True
            elif matrix[midRow][midCol] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
        