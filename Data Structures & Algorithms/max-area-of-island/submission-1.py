class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        currArea = 0
        queue = deque()
        visited = set()
        directions = [(-1,0), (1, 0), (0,-1), (0, 1)]

        # loop through all the rows
        for row in range(len(grid)):
            # loop through all the cols
            for col in range(len(grid[0])):
                # check if row, col has been visited and if it is 1
                if (row, col) not in visited and grid[row][col] == 1:
                    # append to queue and visited
                    queue.append((row, col))
                    visited.add((row, col))
                    # add to current area
                    currArea+=1
                        # while queue exists
                    while queue:
                        # pop the leftmost value
                        r, c = queue.popleft()
                        # loop through directions
                        for nr, nc in directions:
                            # create new row and new column
                            new_row = r + nr
                            new_col = c + nc
                        # check if they are in bounds and "1"
                            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                                if grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                                    # add to visited and queue
                                    visited.add((new_row, new_col))
                                    queue.append((new_row, new_col))
                                    currArea+=1
                    if currArea > maxArea:
                        maxArea = currArea
                    currArea = 0
        # return maxArea
        return maxArea