class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo={}
        def dfs(row, col):
            if row >= len(grid) or col >= len(grid[0]):
                return float('inf')
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return grid[row][col]
            if (row, col) in memo:
                return memo[(row, col)]
            mini = min(dfs(row+1, col), dfs(row, col+1))
            memo[(row, col)] = grid[row][col] + mini
            return memo[(row, col)]
        return dfs(0,0)