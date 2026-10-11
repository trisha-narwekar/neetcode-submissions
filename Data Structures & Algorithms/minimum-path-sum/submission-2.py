class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # memo for saving

        # recursive function
            # base case 1 - check if row >= len(grid) or col >= len(grid[0]):
                # return inf
            # base case 2 - row and col are at the bottom right corner
                # return the cell
            # if the row and col are in memo:
                # return memo
            # check minimum - minimum of dfs(row, col + 1) and dfs(row + 1, col)
            # save to memo
            # return memo
        # return dfs(0, 0)



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